from src.loaders import (
    CSVLoader,
    JSONLoader,
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


if __name__ == "__main__":
    main()