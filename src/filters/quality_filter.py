from typing import List

from src.models import DocumentChunk


class QualityFilter:

    def __init__(self, min_length: int = 50):
        self.min_length = min_length

    def filter(self, chunks: List[DocumentChunk]) -> List[DocumentChunk]:
        filtered = []
        seen = set()

        for chunk in chunks:

            text = chunk.text.strip()

            if not text:
                continue

            if len(text) < self.min_length:
                continue

            if text in seen:
                continue

            seen.add(text)
            filtered.append(chunk)

        return filtered