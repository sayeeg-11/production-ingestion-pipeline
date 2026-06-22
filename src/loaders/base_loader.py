"""
Abstract Base Loader

Every loader in the project must inherit from this class
and implement the `load()` method.
"""

from abc import ABC, abstractmethod

from src.models import BaseDocument


class BaseLoader(ABC):
    """
    Abstract base class for all document loaders.
    """

    @abstractmethod
    def load(self, source: str) -> BaseDocument:
        """
        Load data from the given source and return
        a standardized BaseDocument object.

        Parameters
        ----------
        source : str
            Path to the file or URL.

        Returns
        -------
        BaseDocument
        """
        pass