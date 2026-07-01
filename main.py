from src.pipeline import IngestionPipeline
from src.executor import ParallelExecutor


def main():

    pipeline = IngestionPipeline()

    files = [
        "data/csv/sample.csv",
        "data/json/sample.json",
        "data/pdf/sample.pdf",
        "data/web/urls.txt",
    ]

    executor = ParallelExecutor()

    executor.execute(pipeline.ingest, files)

    pipeline.print_summary()


if __name__ == "__main__":
    main()