"""
JSON Loader
"""

import json
import uuid
from pathlib import Path

from src.loaders.base_loader import BaseLoader
from src.models import BaseDocument, DocumentMetadata
from src.utils.logger import logger


class JSONLoader(BaseLoader):
    """
    Loads JSON documents.
    """

    def load(self, source: str) -> BaseDocument:

        logger.info(f"Loading JSON: {source}")

        with open(source, "r", encoding="utf-8") as file:
            data = json.load(file)

        text = json.dumps(
            data,
            indent=4,
            ensure_ascii=False,
        )

        metadata = DocumentMetadata(
            source="json",
            file_name=Path(source).name,
            file_type=".json",
        )

        return BaseDocument(
            document_id=str(uuid.uuid4()),
            text=text,
            metadata=metadata,
        )