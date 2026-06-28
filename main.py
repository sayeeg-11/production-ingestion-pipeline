from src.pipeline import IngestionPipeline


def main():

    pipeline = IngestionPipeline()

    pipeline.ingest("data/csv/sample.csv")

    pipeline.ingest("data/json/sample.json")

    pipeline.ingest("data/pdf/sample.pdf")

    pipeline.ingest("data/web/urls.txt")


if __name__ == "__main__":
    main()