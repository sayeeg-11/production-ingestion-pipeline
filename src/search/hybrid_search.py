from collections import defaultdict

from src.utils.logger import logger


class HybridSearch:
    """
    Combines FAISS semantic search and BM25 keyword search.
    """

    def __init__(self, faiss_store, bm25_search):

        self.faiss = faiss_store
        self.bm25 = bm25_search

    def search(
        self,
        query_embedding,
        query_text,
        k=5,
        alpha=0.5
    ):

        faiss_results = self.faiss.search(
            query_embedding,
            k=k
        )

        bm25_results = self.bm25.search(
            query_text,
            k=k
        )

        merged = defaultdict(
            lambda: {
                "text": "",
                "metadata": {},
                "score": 0.0
            }
        )

        # -------------------------
        # FAISS Results
        # -------------------------

        for rank, result in enumerate(faiss_results):

            score = alpha * (1 / (rank + 1))

            merged[result["text"]]["text"] = result["text"]
            merged[result["text"]]["metadata"] = result["metadata"]
            merged[result["text"]]["score"] += score

        # -------------------------
        # BM25 Results
        # -------------------------

        for rank, result in enumerate(bm25_results):

            score = (1 - alpha) * (1 / (rank + 1))

            merged[result["text"]]["text"] = result["text"]
            merged[result["text"]]["metadata"] = result["metadata"]
            merged[result["text"]]["score"] += score

        results = sorted(
            merged.values(),
            key=lambda x: x["score"],
            reverse=True
        )

        logger.info(
            f"Hybrid Search returned {len(results)} results."
        )

        return results[:k]