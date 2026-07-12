from src.embeddings import EmbeddingFactory
from src.vectorstores import FAISSStore
from src.search.bm25_search import BM25Search
from src.retrieval.hybrid import HybridSearch


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

    def search(
        self,
        query: str,
        k: int = 5,
    ):

        # Generate embedding
        embedding = self.embedding_model.embed([query])[0]

        # Semantic search
        vector_results = self.vector_store.search(
            embedding,
            k=k,
        )

        # Keyword search
        keyword_results = self.keyword_search.search(
            query,
            k=k,
        )

        # Merge both searches
        results = HybridSearch.merge(
            vector_results,
            keyword_results,
        )

        return results[:k]