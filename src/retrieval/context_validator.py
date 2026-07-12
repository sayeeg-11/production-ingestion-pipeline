class ContextValidator:

    MIN_SCORE = 3.0

    @classmethod
    def has_relevant_context(cls, results):

        if not results:
            return False

        best = results[0]

        return best["score"] >= cls.MIN_SCORE