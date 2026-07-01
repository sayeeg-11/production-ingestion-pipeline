import uuid

from langchain_text_splitters import RecursiveCharacterTextSplitter

from .base_chunker import BaseChunker
from src.models import DocumentChunk


class JSONChunker(BaseChunker):

    def __init__(self):
        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=50,
        )

    def chunk(self, document):

        chunks = self.splitter.split_text(document.text)

        document_chunks = []

        for i, chunk in enumerate(chunks):

            metadata = document.metadata.model_copy(deep=True)
            metadata.chunk_index = i

            document_chunks.append(
                DocumentChunk(
                    chunk_id=str(uuid.uuid4()),
                    document_id=document.document_id,
                    chunk_index=i,
                    text=chunk,
                    metadata=metadata,
                )
            )
        return document_chunks