import hashlib


class VersionManager:

    def generate_hash(self, text: str) -> str:
        return hashlib.sha256(text.encode("utf-8")).hexdigest()

    def get_version(self, text: str) -> str:
        return self.generate_hash(text)