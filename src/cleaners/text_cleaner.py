import re

from .base_cleaner import BaseCleaner


class TextCleaner(BaseCleaner):

    def clean(self, text: str) -> str:

        # Remove multiple spaces
        text = re.sub(r"[ \t]+", " ", text)

        # Remove multiple blank lines
        text = re.sub(r"\n{2,}", "\n", text)

        # Remove leading/trailing whitespace
        text = text.strip()

        return text