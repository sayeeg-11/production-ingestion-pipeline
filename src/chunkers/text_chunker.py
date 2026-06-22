"""
Text Chunker (Production-ready simple version)
"""

import uuid

from typing import List

from src.chunkers.base_chunker import BaseChunker
from src.chunkers.chunking_strategy import ChunkingStrategy
from src.models import BaseDocument, DocumentChunk
from src.config import CHUNK_SIZE, CHUNK_OVERLAP


class TextChunker(BaseChunker):
    """
    Splits text into overlapping chunks.
    """

    def __init__(
        self,
        chunk_size: int = CHUNK_SIZE,
        overlap: int = CHUNK_OVERLAP,
    ):

        self.chunk_size = chunk_size
        self.overlap = overlap

    def _split_text(self, text: str) -> List[str]:

        chunks = []

        start = 0

        while start < len(text):

            end = start + self.chunk_size

            chunks.append(text[start:end])

            start = end - self.overlap

        return chunks

    def chunk(self, document: BaseDocument) -> List[DocumentChunk]:

        raw_chunks = self._split_text(document.text)

        result = []

        for idx, chunk_text in enumerate(raw_chunks):

            chunk = DocumentChunk(
                chunk_id=str(uuid.uuid4()),
                document_id=document.document_id,
                chunk_index=idx,
                text=chunk_text,
                metadata=document.metadata,
            )

            result.append(chunk)

        return result