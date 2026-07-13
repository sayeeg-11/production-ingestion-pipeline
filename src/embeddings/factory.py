from src.config import EMBEDDING_MODEL

from .sentence_transformer import SentenceTransformerEmbedding


class EmbeddingFactory:
    """
    Factory responsible for creating embedding models.
    """

    @staticmethod
    def create():


        return SentenceTransformerEmbedding(
            model_name=EMBEDDING_MODEL,
        )