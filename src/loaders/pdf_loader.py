"""
PDF Loader
"""

import uuid
from pathlib import Path

import fitz

from src.loaders.base_loader import BaseLoader
from src.models import BaseDocument, DocumentMetadata
from src.utils.logger import logger


class PDFLoader(BaseLoader):
    """
    Loads PDF documents using PyMuPDF.
    """

    def load(self, source: str) -> BaseDocument:

        logger.info(f"Loading PDF: {source}")

        pdf = fitz.open(source)

        pages = []
        total_pages = len(pdf)

        for page in pdf:
            pages.append(page.get_text())

        pdf.close()

        text = "\n".join(pages)

        metadata = DocumentMetadata(
            source="pdf",
            file_name=Path(source).name,
            file_type=".pdf",
            page_number=total_pages,
        )

        return BaseDocument(
            document_id=str(uuid.uuid4()),
            text=text,
            metadata=metadata,
        )