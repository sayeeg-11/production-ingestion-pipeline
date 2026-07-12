import faiss
import pickle
import numpy as np
from pathlib import Path
from src.config import VECTOR_DB_DIRECTORY
from src.utils.logger import logger


class FAISSStore:
    """
    Handles storing, loading and searching vector embeddings using FAISS.
    """

    def __init__(self):

        self.dimension = None
        self.index = None
        self.metadata = []

        self.db_path = VECTOR_DB_DIRECTORY
        self.db_path.mkdir(exist_ok=True)

        self.index_file = self.db_path / "index.faiss"
        self.metadata_file = self.db_path / "metadata.pkl"

    def add(self, chunks):

        if not chunks:
            logger.warning("No chunks received for vector storage.")
            return

        # -----------------------------
        # Validate embeddings
        # -----------------------------
        valid_embeddings = []
        valid_chunks = []

        for chunk in chunks:

            if chunk.embedding is None:
                logger.warning(
                    f"Skipping chunk {chunk.chunk_id}: embedding is None."
                )
                continue

            embedding = np.asarray(
                chunk.embedding,
                dtype=np.float32
            ).flatten()

            if embedding.size == 0:
                logger.warning(
                    f"Skipping chunk {chunk.chunk_id}: empty embedding."
                )
                continue

            valid_embeddings.append(embedding)
            valid_chunks.append(chunk)

        if not valid_embeddings:
            logger.warning("No valid embeddings found.")
            return

        embeddings = np.vstack(valid_embeddings)

        logger.info(f"Embedding matrix shape: {embeddings.shape}")

        # -----------------------------
        # Create index
        # -----------------------------
        if self.index is None:

            self.dimension = embeddings.shape[1]
            self.index = faiss.IndexFlatL2(self.dimension)

            logger.info(
                f"Created FAISS index (dimension={self.dimension})"
            )
            # -----------------------------
            # Prevent duplicate vectors
            # -----------------------------

            existing_ids = {
                item["metadata"]["chunk_id"]
                for item in self.metadata
            }

            new_embeddings = []
            new_metadata = []

            for embedding, chunk in zip(valid_embeddings, valid_chunks):

                chunk_id = chunk.chunk_id

                if chunk_id in existing_ids:
                    continue

                new_embeddings.append(embedding)

                new_metadata.append(
                    {
                        "text": chunk.text,
                        "metadata": chunk.metadata.model_dump()
                    }
                )

            if not new_embeddings:

                logger.info("No new vectors to add.")
                return

            new_embeddings = np.vstack(new_embeddings)

            self.index.add(new_embeddings)

            self.metadata.extend(new_metadata)

            logger.info(
                f"Added {len(new_metadata)} new vectors."
            )


    def save(self):

        if self.index is None:
            logger.warning("Nothing to save.")
            return

        faiss.write_index(
            self.index,
            str(self.index_file)
        )

        with open(self.metadata_file, "wb") as f:
            pickle.dump(self.metadata, f)

        logger.info("FAISS index saved successfully.")

    def load(self):

        if not self.index_file.exists():
            logger.warning("No FAISS index found.")
            return

        self.index = faiss.read_index(
            str(self.index_file)
        )

        self.dimension = self.index.d

        with open(self.metadata_file, "rb") as f:
            self.metadata = pickle.load(f)

        logger.info(
            f"Loaded FAISS index ({self.index.ntotal} vectors)"
        )

    def search(self, query_embedding, k=5):

        if self.index is None:
            raise ValueError("FAISS index is empty.")

        query = np.asarray(
            query_embedding,
            dtype=np.float32
        ).reshape(1, -1)

        distances, indices = self.index.search(query, k)

        results = []

        for distance, idx in zip(distances[0], indices[0]):

            if idx == -1:
                continue

            results.append(
                {
                    "score": float(distance),
                    "text": self.metadata[idx]["text"],
                    "metadata": self.metadata[idx]["metadata"],
                }
            )

        return results