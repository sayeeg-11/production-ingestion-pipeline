from typing import List


class HybridSearch:
    """
    Merges results from multiple retrieval systems.

    Current Strategy:
    -----------------
    - Merge FAISS + BM25 results
    - Remove duplicates
    - Keep highest score

    Future:
    -------
    - Weighted Hybrid Search
    - Reciprocal Rank Fusion (RRF)
    - Cross Encoder Re-ranking
    """

    @staticmethod
    def merge(
        vector_results: List[dict],
        keyword_results: List[dict],
    ) -> List[dict]:

        merged = {}

        for result in vector_results + keyword_results:

            key = result["text"]

            if (
                key not in merged
                or result["score"] > merged[key]["score"]
            ):
                merged[key] = result

        return sorted(
            merged.values(),
            key=lambda x: x["score"],
            reverse=True,
        )