import json
from pathlib import Path


class ChunkStorage:

    def __init__(self):

        self.output = Path("output")

        self.output.mkdir(exist_ok=True)

    def save(self, chunks, filename):

        file = self.output / f"{filename}.json"

        with open(file, "w", encoding="utf-8") as f:

            json.dump(
                [chunk.model_dump() for chunk in chunks],
                f,
                indent=4,
                ensure_ascii=False,
            )