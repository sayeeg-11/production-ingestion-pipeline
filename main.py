from src.loaders import CSVLoader, JSONLoader, PDFLoader, WebLoader

from src.chunkers import  CSVChunker, JSONChunker, PDFChunker, WebChunker
from src.utils.logger import logger

from src.filters import QualityFilter


def main():

    # ---------------- CSV ----------------
    logger.info("Loading CSV...")
    csv_loader = CSVLoader()
    csv_doc = csv_loader.load("data/csv/sample.csv")

    csv_chunker = CSVChunker()
    csv_chunks = csv_chunker.chunk(csv_doc)

    logger.info(f"CSV Chunks: {len(csv_chunks)}")
    print(csv_chunks[0].model_dump(exclude={"text"}))
    
    filterer = QualityFilter()

    csv_chunks = filterer.filter(csv_chunks)

    # ---------------- JSON ----------------
    logger.info("Loading JSON...")
    json_loader = JSONLoader()
    json_doc = json_loader.load("data/json/sample.json")

    json_chunker = JSONChunker()
    json_chunks = json_chunker.chunk(json_doc)

    logger.info(f"JSON Chunks: {len(json_chunks)}")
    print(json_chunks[0].model_dump(exclude={"text"}))
    
    json_chunks = filterer.filter(json_chunks)

    # ---------------- PDF ----------------
    logger.info("Loading PDF...")
    pdf_loader = PDFLoader()
    pdf_doc = pdf_loader.load("data/pdf/sample.pdf")

    pdf_chunker = PDFChunker()
    pdf_chunks = pdf_chunker.chunk(pdf_doc)

    logger.info(f"PDF Chunks: {len(pdf_chunks)}")
    print(pdf_chunks[0].model_dump(exclude={"text"}))
    
    pdf_chunks = filterer.filter(pdf_chunks)

    # ---------------- WEB ----------------
    logger.info("Loading Web...")
    web_loader = WebLoader()
    web_docs = web_loader.load("data/web/urls.txt")

    web_chunker = WebChunker()

    for doc in web_docs:
        chunks = web_chunker.chunk(doc)
        logger.info(f"Web Chunks: {len(chunks)}")
        print(chunks[0].model_dump(exclude={"text"}))
        chunks = filterer.filter(chunks) 


if __name__ == "__main__":
    main()