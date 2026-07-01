from src.chunkers import (
    CSVChunker,
    JSONChunker,
    PDFChunker,
    WebChunker,
)


class ChunkerRegistry:

    def __init__(self):

        self._chunkers = {
            ".csv": CSVChunker(),
            ".json": JSONChunker(),
            ".pdf": PDFChunker(),
            ".txt": WebChunker(),
        }

    def get_chunker(self, extension):

        return self._chunkers.get(extension)