class ContextValidator:
    """
    Checks whether the retrieved context is relevant enough
    to answer the user's question.
    """

    MIN_SCORE = 3.0

    @classmethod
    def has_relevant_context(cls, results):

        if not results:
            return False

        best = results[0]

        return best["rerank_score"] >= cls.MIN_SCORE