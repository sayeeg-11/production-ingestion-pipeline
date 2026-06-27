from src.loaders import (
    CSVLoader,
    JSONLoader,
    PDFLoader,
    pdf_loader,
    WebLoader,
    web_loader,
)

from src.utils.logger import logger


def main():

    logger.info("Loading CSV...")

    csv_doc = CSVLoader().load(
        "data/csv/sample.csv"
    )

    print(csv_doc.model_dump())

    logger.info("Loading JSON...")

    json_doc = JSONLoader().load(
        "data/json/sample.json"
    )

    print(json_doc.model_dump())

    pdf_loader = PDFLoader()
    
    logger.info("Loading PDF...")
    
    pdf_doc = pdf_loader.load("data/pdf/sample.pdf")
    print(pdf_doc.model_dump())  
    
    web_loader = WebLoader()
    logger.info("Loading Web Pages...")

    web_docs = web_loader.load("data/web/urls.txt")

    for doc in web_docs:
        print(doc.model_dump()) 

if __name__ == "__main__":
    main()