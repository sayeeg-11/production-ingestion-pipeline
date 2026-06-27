from pathlib import Path

import requests
from bs4 import BeautifulSoup

from .base_loader import BaseLoader
from src.models import BaseDocument, DocumentMetadata
from src.utils.logger import logger

import uuid


class WebLoader(BaseLoader):
    def load(self, file_path: str):
        logger.info(f"Loading URLs from: {file_path}")

        documents = []

        with open(file_path, "r", encoding="utf-8") as file:
            urls = [line.strip() for line in file if line.strip()]

        for url in urls:
            try:
                headers = {
                    "User-Agent": "Mozilla/5.0"
                }

                response = requests.get(
                url,
                headers=headers,
                timeout=10,
                )
                response.raise_for_status()

                soup = BeautifulSoup(response.text, "lxml")

                for tag in soup(["script", "style", "nav", "footer", "header"]):
                    tag.decompose()

                text = soup.get_text(separator=" ", strip=True)

                metadata = DocumentMetadata(
                    source="web",
                    file_name=Path(file_path).name,
                    file_type=".txt",
                    url=url,
                )

                documents.append(
                    BaseDocument(
                        document_id=str(uuid.uuid4()),
                        text=text,
                        metadata=metadata,
                    )
                )

            except Exception as e:
                logger.error(f"Failed to load {url}: {e}")

        return documents