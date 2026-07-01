from src.loaders import (
    CSVLoader,
    JSONLoader,
    PDFLoader,
    WebLoader,
)


class LoaderRegistry:

    def __init__(self):

        self._loaders = {
            ".csv": CSVLoader(),
            ".json": JSONLoader(),
            ".pdf": PDFLoader(),
            ".txt": WebLoader(),
        }

    def get_loader(self, extension):

        return self._loaders.get(extension)