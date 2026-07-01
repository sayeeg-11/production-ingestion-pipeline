"""
Metadata Model
"""

from typing import Optional

from pydantic import BaseModel, Field


class DocumentMetadata(BaseModel):

    # ==========================================================
    # Source Information
    # ==========================================================

    source: str = Field(...)

    file_name: str = Field(...)

    file_type: str = Field(...)

    # ==========================================================
    # File Metadata
    # ==========================================================

    created_at: Optional[str] = None

    modified_at: Optional[str] = None

    author: Optional[str] = None

    page_number: Optional[int] = None

    url: Optional[str] = None

    language: Optional[str] = None

    # ==========================================================
    # Pipeline Metadata
    # ==========================================================

    version: Optional[str] = None

    ingested_at: Optional[str] = None

    chunk_index: Optional[int] = None

    total_chunks: Optional[int] = None

    processing_status: Optional[str] = None