from sentence_transformers import CrossEncoder


class Reranker:
    """
    Cross Encoder reranker.

    Scores (query, chunk) pairs and returns
    the most relevant chunks.
    """

    def __init__(self):

        self.model = CrossEncoder(
            "cross-encoder/ms-marco-MiniLM-L-6-v2"
        )

    def rerank(
        self,
        query,
        chunks,
        top_k=5,
    ):

        if not chunks:
            return []

        pairs = [
            (query, chunk["text"])
            for chunk in chunks
        ]

        scores = self.model.predict(pairs)

        for chunk, score in zip(chunks, scores):
            chunk["rerank_score"] = float(score)

        chunks.sort(
            key=lambda x: x["rerank_score"],
            reverse=True,
        )

        return chunks[:top_k]