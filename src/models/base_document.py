"""
Base Document Model
"""

from pydantic import BaseModel

from src.models.metadata import DocumentMetadata


class BaseDocument(BaseModel):

    document_id: str

    text: str

    metadata: DocumentMetadata