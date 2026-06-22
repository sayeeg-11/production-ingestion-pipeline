from src.models import (
    BaseDocument,
    DocumentMetadata,
)

metadata = DocumentMetadata(
    source="pdf",
    file_name="sample.pdf",
    file_type=".pdf",
    author="Sayee",
)

document = BaseDocument(
    document_id="doc_001",
    text="Hello World",
    metadata=metadata,
)

print(document.model_dump())