import uuid
import fitz
from pathlib import Path

from .base_loader import BaseLoader
from src.models import BaseDocument, DocumentMetadata
from src.utils.logger import logger


class PDFLoader(BaseLoader):
    def load(self, file_path: str) -> BaseDocument:
        logger.info(f"Loading PDF: {file_path}")

        path = Path(file_path)

        document = fitz.open(file_path)

        text = ""

        for page in document:
            text += page.get_text()

        metadata = DocumentMetadata(
            source="pdf",
            file_name=path.name,
            file_type=path.suffix,
            page_number=document.page_count,
        )

        return BaseDocument(
            document_id=str(uuid.uuid4()),
            text=text,
            metadata=metadata,
        )   