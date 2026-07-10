"""
Chunk Model
"""

from pydantic import BaseModel
from typing import Optional
from src.models.metadata import DocumentMetadata


class DocumentChunk(BaseModel):

    chunk_id: str

    document_id: str

    chunk_index: int

    text: str

    metadata: DocumentMetadata
    
    embedding: Optional[list[float]] = None