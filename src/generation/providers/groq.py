from openai import OpenAI

from src.config import (
    GROQ_API_KEY,
    GROQ_MODEL,
)

from src.generation.base import BaseGenerator


class GroqGenerator(BaseGenerator):
    """
    Groq LLM implementation.
    """

    def __init__(self):

        self.client = OpenAI(
            api_key=GROQ_API_KEY,
            base_url="https://api.groq.com/openai/v1",
        )

        self.model = GROQ_MODEL

    def generate(
        self,
        prompt: str,
        temperature: float = 0.2,
        max_tokens: int = 1024,
    ) -> str:

        response = self.client.chat.completions.create(
            model=self.model,
            temperature=temperature,
            max_tokens=max_tokens,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
        )

        return response.choices[0].message.content.strip()