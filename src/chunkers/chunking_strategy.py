"""
Chunking Strategy Definitions
"""

from enum import Enum


class ChunkingStrategy(str, Enum):
    """
    Different strategies for chunking text.
    """

    FIXED_SIZE = "fixed_size"
    SENTENCE = "sentence"
    PARAGRAPH = "paragraph"