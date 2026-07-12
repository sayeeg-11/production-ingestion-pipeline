class PromptBuilder:
    """
    Builds prompts for Retrieval-Augmented Generation (RAG).

    Responsibilities
    ----------------
    - Combine retrieved context
    - Add user question
    - Produce a clean prompt for the LLM
    """

    SYSTEM_PROMPT = """
You are a helpful AI assistant.

Answer ONLY using the provided context.

If the answer cannot be found in the context,
respond with:

"I couldn't find that information in the provided documents."

Do not make up facts.
""".strip()

    @classmethod
    def build(
        cls,
        query: str,
        chunks: list,
    ) -> str:

        context = []

        for i, chunk in enumerate(chunks, start=1):

            context.append(
                f"[Document {i}]\n{chunk['text']}"
            )

        context = "\n\n".join(context)

        prompt = f"""
{cls.SYSTEM_PROMPT}

------------------------
Context
------------------------

{context}

------------------------
Question
------------------------

{query}

------------------------
Answer
------------------------
"""

        return prompt.strip()