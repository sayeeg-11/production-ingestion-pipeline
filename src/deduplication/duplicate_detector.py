import hashlib
import pickle

from src.config import STORAGE_DIRECTORY
from src.utils.logger import logger


class DuplicateDetector:
    """
    Detects duplicate chunks using SHA256 hashes.
    """

    def __init__(self):
        self.hashes = set()

        self.hash_file = STORAGE_DIRECTORY / "duplicates.pkl"

        self.load()

    def _get_hash(self, text: str) -> str:
        """
        Generate SHA256 hash for chunk text.
        """

        return hashlib.sha256(
            text.strip().encode("utf-8")
        ).hexdigest()

    def is_duplicate(self, text: str) -> bool:
        """
        Check if chunk already exists.
        """

        chunk_hash = self._get_hash(text)

        return chunk_hash in self.hashes

    def add(self, text: str):
        """
        Store chunk hash.
        """

        chunk_hash = self._get_hash(text)

        self.hashes.add(chunk_hash)

    def filter(self, chunks):
        """
        Remove duplicate chunks.
        """

        unique_chunks = []

        for chunk in chunks:

            if self.is_duplicate(chunk.text):
                continue

            self.add(chunk.text)

            unique_chunks.append(chunk)

        logger.info(
            f"Duplicate Filter: kept {len(unique_chunks)} / {len(chunks)} chunks"
        )

        return unique_chunks

    def save(self):

        with open(self.hash_file, "wb") as f:
            pickle.dump(self.hashes, f)

    def load(self):

        if not self.hash_file.exists():
            return

        with open(self.hash_file, "rb") as f:
            self.hashes = pickle.load(f)

        logger.info(
            f"Loaded {len(self.hashes)} known chunk hashes."
        )