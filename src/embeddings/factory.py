from .sentence_transformer import SentenceTransformerEmbedding


class EmbeddingFactory:

    @staticmethod
    def create(model="sentence-transformer"):

        if model == "sentence-transformer":
            return SentenceTransformerEmbedding()

        raise ValueError(f"Unsupported embedding model: {model}")