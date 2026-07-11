from pathlib import Path
from datetime import datetime
from src.deduplication import DuplicateDetector
from src.registry import LoaderRegistry, ChunkerRegistry
from src.filters import QualityFilter
from src.versioning import VersionManager
from src.storage import ChunkStorage
from src.cleaners import TextCleaner
from src.cache import VersionCache
from src.utils.logger import logger
from src.monitoring import PipelineStats
from src.embeddings import EmbeddingFactory
from src.vectorstores import FAISSStore


class IngestionPipeline:

    def __init__(self):

        self.loader_registry = LoaderRegistry()
        self.chunker_registry = ChunkerRegistry()

        self.cleaner = TextCleaner()
        self.filter = QualityFilter()
        self.duplicate_detector = DuplicateDetector()

        self.version = VersionManager()
        self.cache = VersionCache()

        self.storage = ChunkStorage()

        self.embedding_model = EmbeddingFactory.create()

        self.vector_store = FAISSStore()
        self.vector_store.load()

        self.stats = PipelineStats()

    def ingest(self, file_path: str):

        try:

            extension = Path(file_path).suffix.lower()

            loader = self.loader_registry.get_loader(extension)

            if loader is None:
                logger.error(f"Unsupported file type: {extension}")
                self.stats.increment_failures()
                return []

            logger.info(f"Ingesting {file_path}")

            documents = loader.load(file_path)

            if not isinstance(documents, list):
                documents = [documents]

            all_chunks = []

            for document in documents:

                try:

                    # ----------------------------------------
                    # Clean document
                    # ----------------------------------------

                    document.text = self.cleaner.clean(document.text)

                    # ----------------------------------------
                    # Versioning
                    # ----------------------------------------

                    version = self.version.get_version(document.text)

                    if self.cache.is_processed(
                        document.metadata.file_name,
                        version,
                    ):
                        logger.info(
                            f"Skipping {document.metadata.file_name} (unchanged)"
                        )
                        self.stats.increment_skipped()
                        continue

                    document.metadata.version = version
                    document.metadata.ingested_at = datetime.now().isoformat()
                    document.metadata.processing_status = "processed"

                    logger.info(f"Version: {version}")

                    # ----------------------------------------
                    # Chunking
                    # ----------------------------------------

                    chunker = self.chunker_registry.get_chunker(extension)

                    chunks = chunker.chunk(document)
                    chunks = self.duplicate_detector.filter(chunks)

                    # ----------------------------------------
                    # Quality Filter
                    # ----------------------------------------

                    before_filter = len(chunks)

                    chunks = self.filter.filter(chunks)

                    after_filter = len(chunks)

                    self.stats.add_created_chunks(after_filter)
                    self.stats.add_filtered_chunks(
                        before_filter - after_filter
                    )

                    if not chunks:
                        logger.warning(
                            f"No valid chunks found for {document.metadata.file_name}"
                        )
                        continue

                    # ----------------------------------------
                    # Generate Embeddings
                    # ----------------------------------------

                    texts = [chunk.text for chunk in chunks]

                    embeddings = self.embedding_model.embed(texts)

                    for chunk, embedding in zip(chunks, embeddings):
                        chunk.embedding = embedding

                    logger.info(
                        f"Generated {len(embeddings)} embeddings "
                        f"(dimension={len(embeddings[0])}) "
                        f"for {document.metadata.file_name}"
                    )

                    # ----------------------------------------
                    # Metadata enrichment
                    # ----------------------------------------

                    total_chunks = len(chunks)

                    for chunk in chunks:
                        chunk.metadata.total_chunks = total_chunks

                    # ----------------------------------------
                    # Store vectors in FAISS
                    # ----------------------------------------

                    self.vector_store.add(chunks)

                    logger.info(f"Chunks: {len(chunks)}")

                    all_chunks.extend(chunks)

                    # ----------------------------------------
                    # Update cache
                    # ----------------------------------------

                    self.cache.update(
                        document.metadata.file_name,
                        version,
                    )

                except Exception as e:
                    logger.exception(f"Document processing failed: {e}")
                    self.stats.increment_failures()

            # ----------------------------------------
            # Save outputs
            # ----------------------------------------

            self.vector_store.save()
            self.duplicate_detector.save()

            output_name = Path(file_path).stem

            self.storage.save(all_chunks, output_name)

            logger.info(f"Finished processing {file_path}")

            self.stats.increment_processed()

            return all_chunks

        except Exception as e:
            logger.exception(f"Pipeline failed: {e}")
            self.stats.increment_failures()
            return []

    def print_summary(self):

        print("\n" + "=" * 45)
        print("        PIPELINE SUMMARY")
        print("=" * 45)

        print(f"Files Processed : {self.stats.files_processed}")
        print(f"Files Skipped   : {self.stats.files_skipped}")
        print(f"Chunks Created  : {self.stats.chunks_created}")
        print(f"Chunks Filtered : {self.stats.chunks_filtered}")
        print(f"Failures        : {self.stats.failures}")

        print("=" * 45)