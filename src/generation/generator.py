class Generator:
    """
    Responsible for generating the final prompt
    (LLM integration comes next).
    """

    def build_prompt(
        self,
        query: str,
        chunks: list,
    ) -> str:

        context = ""

        for i, chunk in enumerate(chunks, start=1):

            context += (
                f"Chunk {i}\n"
                f"{chunk['text']}\n\n"
            )

        prompt = f"""
You are a helpful AI assistant.

Use ONLY the context below to answer the user's question.

If the answer is not present in the context,
say you don't know.

Context
-------

{context}

Question:
{query}

Answer:
"""

        return prompt

    def generate(
        self,
        query: str,
        chunks: list,
    ):

        return self.build_prompt(
            query,
            chunks,
        )