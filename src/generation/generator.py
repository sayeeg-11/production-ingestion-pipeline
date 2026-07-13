from src.generation.providers.groq import GroqGenerator


class Generator:
    """
    Builds the prompt and generates
    the final answer using the LLM.
    """

    def __init__(self):

        self.llm = GroqGenerator()

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
    ) -> str:

        prompt = self.build_prompt(
            query=query,
            chunks=chunks,
        )

        response = self.llm.generate(
            prompt=prompt,
        )

        return response