"""
Web Loader
"""

import uuid

import requests
from bs4 import BeautifulSoup

from src.loaders.base_loader import BaseLoader
from src.models import BaseDocument, DocumentMetadata
from src.utils.logger import logger


class WebLoader(BaseLoader):
    """
    Loads text from web pages.
    """

    def load(self, source: str) -> BaseDocument:

        logger.info(f"Loading Web Page: {source}")

        response = requests.get(
            source,
            timeout=15,
            headers={
                "User-Agent": (
                    "Mozilla/5.0 "
                    "(Windows NT 10.0; Win64; x64)"
                )
            },
        )

        response.raise_for_status()

        soup = BeautifulSoup(
            response.text,
            "lxml",
        )

        text = soup.get_text(
            separator="\n",
            strip=True,
        )

        metadata = DocumentMetadata(
            source="web",
            file_name=source,
            file_type=".html",
            url=source,
        )

        return BaseDocument(
            document_id=str(uuid.uuid4()),
            text=text,
            metadata=metadata,
        )