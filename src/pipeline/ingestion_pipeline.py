from pathlib import Path

from src.loaders import (
    CSVLoader,
    JSONLoader,
    PDFLoader,
    WebLoader,
)

from src.chunkers import (
    CSVChunker,
    JSONChunker,
    PDFChunker,
    WebChunker,
)

from src.filters import QualityFilter
from src.versioning import VersionManager
from src.storage import ChunkStorage
from src.utils.logger import logger


class IngestionPipeline:

    def __init__(self):

        self.loaders = {
            ".csv": CSVLoader(),
            ".json": JSONLoader(),
            ".pdf": PDFLoader(),
            ".txt": WebLoader(),
        }

        self.chunkers = {
            ".csv": CSVChunker(),
            ".json": JSONChunker(),
            ".pdf": PDFChunker(),
            ".txt": WebChunker(),
        }

        self.filter = QualityFilter()
        self.version = VersionManager()
        self.storage = ChunkStorage()

    def ingest(self, file_path: str):

        try:

            extension = Path(file_path).suffix.lower()

            loader = self.loaders.get(extension)

            if loader is None:
                logger.error(f"Unsupported file type: {extension}")
                return []

            logger.info(f"Ingesting {file_path}")

            documents = loader.load(file_path)

            if not isinstance(documents, list):
                documents = [documents]

            all_chunks = []

            for document in documents:

                try:

                    version = self.version.get_version(document.text)
                    logger.info(f"Version: {version}")

                    chunker = self.chunkers[extension]

                    chunks = chunker.chunk(document)
                    chunks = self.filter.filter(chunks)

                    logger.info(f"Chunks: {len(chunks)}")

                    all_chunks.extend(chunks)

                except Exception as e:
                    logger.exception(f"Document processing failed: {e}")

            filename = Path(file_path).stem
            self.storage.save(all_chunks, filename)

            logger.info(f"Finished processing {file_path}")

            return all_chunks

        except Exception as e:
            logger.exception(f"Pipeline failed: {e}")
            return []