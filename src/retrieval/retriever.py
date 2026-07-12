from src.embeddings import EmbeddingFactory
from src.vectorstores import FAISSStore
from src.search.bm25_search import BM25Search
from src.retrieval.hybrid import HybridSearch
from src.reranking import Reranker


class Retriever:
    """
    Coordinates the retrieval process.

    Responsibilities:
    -----------------
    - Generate query embeddings
    - Retrieve semantic results (FAISS)
    - Retrieve keyword results (BM25)
    - Merge both result sets
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
        k: int = 5,
    ):

    # Generate query embedding
        embedding = self.embedding_model.embed([query])[0]

    # Retrieve more candidates for reranking
        vector_results = self.vector_store.search(
            embedding,
            k=20,
    )

        keyword_results = self.keyword_search.search(
            query,
            k=20,
    )

    # Merge semantic + keyword results
        merged_results = HybridSearch.merge(
            vector_results,
            keyword_results,
    )

    # Rerank using Cross Encoder
        reranked = self.reranker.rerank(
            query,
            merged_results,
)           

        return reranked[:k]
    