from abc import ABC, abstractmethod


class BaseGenerator(ABC):
    """
    Base interface for all LLM providers.

    Every provider (Groq, OpenAI, Ollama,
    Gemini, NVIDIA, etc.) must implement
    this interface.
    """

    @abstractmethod
    def generate(
        self,
        prompt: str,
        temperature: float = 0.2,
        max_tokens: int = 1024,
    ) -> str:
        """
        Generate a response from the LLM.

        Parameters
        ----------
        prompt : str
            Prompt sent to the model.

        temperature : float
            Controls randomness.

        max_tokens : int
            Maximum number of output tokens.

        Returns
        -------
        str
            Generated response.
        """
        pass