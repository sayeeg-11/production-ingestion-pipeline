from sentence_transformers import SentenceTransformer

from .base import BaseEmbedding


class SentenceTransformerEmbedding(BaseEmbedding):
    """
    Sentence Transformer embedding model.
    """

    def __init__(self, model_name: str):
        self.model = SentenceTransformer(model_name)

    def embed(self, texts: list[str]) -> list[list[float]]:
        embeddings = self.model.encode(
            texts,
            convert_to_numpy=True,
            show_progress_bar=False,
        )

        return embeddings.tolist()