"""
Base Chunker (Abstract)
"""

from abc import ABC, abstractmethod

from typing import List

from src.models import BaseDocument, DocumentChunk


class BaseChunker(ABC):
    """
    All chunkers must inherit this class.
    """

    @abstractmethod
    def chunk(self, document: BaseDocument) -> List[DocumentChunk]:
        """
        Convert document into chunks.
        """
        pass