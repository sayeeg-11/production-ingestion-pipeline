from src.loaders import CSVLoader
from src.chunkers import TextChunker


loader = CSVLoader()

doc = loader.load("data/csv/sample.csv")

chunker = TextChunker(
    chunk_size=50,
    overlap=10
)

chunks = chunker.chunk(doc)

for c in chunks:
    print("-" * 50)
    print("CHUNK ID:", c.chunk_id)
    print("INDEX:", c.chunk_index)
    print(c.text)