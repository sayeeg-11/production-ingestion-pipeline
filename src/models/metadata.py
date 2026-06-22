"""
Metadata Model
"""

from pydantic import BaseModel, Field

from typing import Optional


class DocumentMetadata(BaseModel):

    source: str = Field(...)

    file_name: str = Field(...)

    file_type: str = Field(...)

    created_at: Optional[str] = None

    modified_at: Optional[str] = None

    author: Optional[str] = None

    page_number: Optional[int] = None

    url: Optional[str] = None

    language: Optional[str] = None