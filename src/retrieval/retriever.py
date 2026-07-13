from numpy import rint
from torch import chunk

from src.embeddings import EmbeddingFactory
from src.vectorstores import FAISSStore
from src.search.bm25_search import BM25Search
from src.retrieval.hybrid import HybridSearch
from src.reranking import Reranker

from src.config import (
    RETRIEVAL_TOP_K,
    RERANK_TOP_K,
    RETRIEVAL_CANDIDATES,
)


class Retriever:
    """
    Coordinates the retrieval process.

    Responsibilities
    ----------------
    - Generate query embeddings
    - Retrieve semantic results (FAISS)
    - Retrieve keyword results (BM25)
    - Merge both result sets
    - Rerank merged results
    """

    def __init__(self):

        self.embedding_model = EmbeddingFactory.create()

        self.vector_store = FAISSStore()
        self.vector_store.load()

        self.keyword_search = BM25Search()

        self.reranker = Reranker()

    def search(
        self,
        query: str,
        k: int | None = None,
    ):

        if k is None:
            k = RETRIEVAL_TOP_K

        # Generate query embedding
        embedding = self.embedding_model.embed([query])[0]

        # Retrieve more candidates for reranking
        vector_results = self.vector_store.search(
            embedding,
            k=RETRIEVAL_CANDIDATES,
        )

        keyword_results = self.keyword_search.search(
            query,
            k=RETRIEVAL_CANDIDATES,
        )

        # Merge semantic + keyword results
        merged_results = HybridSearch.merge(
            vector_results,
            keyword_results,
        )
        print(f"\nVector results : {len(vector_results)}")
        print(f"Keyword results: {len(keyword_results)}")
        print(f"Merged results : {len(merged_results)}")

        # Rerank using Cross Encoder
        reranked = self.reranker.rerank(
            query=query,
            chunks=merged_results,
            top_k=RERANK_TOP_K,
        )
        print(f"Reranked results: {len(reranked)}")
        
        
        print("\nTop reranked scores")

        for chunk in reranked:
            print(chunk["rerank_score"])

        return reranked[:k]