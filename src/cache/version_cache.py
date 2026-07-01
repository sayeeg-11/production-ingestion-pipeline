import json
from pathlib import Path


class VersionCache:

    def __init__(self):

        self.cache_file = Path("cache/versions.json")

        self.cache_file.parent.mkdir(exist_ok=True)

        if not self.cache_file.exists():
            self.cache_file.write_text("{}")

        with open(self.cache_file, "r") as f:
            self.cache = json.load(f)

    def is_processed(self, filename, version):

        return self.cache.get(filename) == version

    def update(self, filename, version):

        self.cache[filename] = version

        with open(self.cache_file, "w") as f:
            json.dump(self.cache, f, indent=4)