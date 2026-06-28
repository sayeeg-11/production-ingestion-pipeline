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

        return [
            DocumentChunk(
                chunk_id=str(uuid.uuid4()),
                chunk_index=i,
                document_id=document.document_id,
                text=chunk,
                metadata=document.metadata,
            )
            for i, chunk in enumerate(chunks)
        ]