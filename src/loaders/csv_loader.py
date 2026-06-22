"""
CSV Loader
"""

import uuid
from pathlib import Path

import pandas as pd

from src.loaders.base_loader import BaseLoader
from src.models import BaseDocument, DocumentMetadata
from src.utils.logger import logger


class CSVLoader(BaseLoader):
    """
    Loads CSV files.
    """

    def load(self, source: str) -> BaseDocument:

        logger.info(f"Loading CSV: {source}")

        dataframe = pd.read_csv(source)

        text = dataframe.to_string(index=False)

        metadata = DocumentMetadata(
            source="csv",
            file_name=Path(source).name,
            file_type=".csv",
        )

        return BaseDocument(
            document_id=str(uuid.uuid4()),
            text=text,
            metadata=metadata,
        )