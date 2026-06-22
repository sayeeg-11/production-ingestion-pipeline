from src.loaders import (
    CSVLoader,
    JSONLoader,
)

csv_loader = CSVLoader()

csv_doc = csv_loader.load(
    "data/csv/sample.csv"
)

print(csv_doc.model_dump())

print("-" * 80)

json_loader = JSONLoader()

json_doc = json_loader.load(
    "data/json/sample.json"
)

print(json_doc.model_dump())