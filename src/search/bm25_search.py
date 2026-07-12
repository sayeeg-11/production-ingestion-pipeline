from pathlib import Path
import pickle

from rank_bm25 import BM25Okapi

from src.config import STORAGE_DIRECTORY
from src.utils.logger import logger


class BM25Search:
    """
    BM25 keyword search index.
    """

    def __init__(self):

        self.documents = []
        self.tokenized_documents = []
        self.index = None

        self.index_file = STORAGE_DIRECTORY / "bm25.pkl"

        self.load()

    def add(self, chunks):

        if not chunks:
            return

        for chunk in chunks:

            self.documents.append(
                {
                    "text": chunk.text,
                    "metadata": chunk.metadata.model_dump()
                }
            )

            self.tokenized_documents.append(
                chunk.text.lower().split()
            )

        self.index = BM25Okapi(self.tokenized_documents)

        logger.info(
            f"BM25 indexed {len(chunks)} chunks."
        )

    def search(self, query, k=5):

        if self.index is None:
            return []

        scores = self.index.get_scores(
            query.lower().split()
        )

        ranked = sorted(
            enumerate(scores),
            key=lambda x: x[1],
            reverse=True
        )[:k]

        results = []

        for idx, score in ranked:

            results.append(
                {
                    "score": float(score),
                    "text": self.documents[idx]["text"],
                    "metadata": self.documents[idx]["metadata"]
                }
            )

        return results

    def save(self):

        with open(self.index_file, "wb") as f:

            pickle.dump(
                (
                    self.documents,
                    self.tokenized_documents
                ),
                f
            )

        logger.info("BM25 index saved.")

    def load(self):

        if not self.index_file.exists():
            return

        with open(self.index_file, "rb") as f:

            self.documents, self.tokenized_documents = pickle.load(f)

        if self.tokenized_documents:

            self.index = BM25Okapi(
                self.tokenized_documents
            )

        logger.info(
            f"Loaded BM25 index ({len(self.documents)} documents)"
        )