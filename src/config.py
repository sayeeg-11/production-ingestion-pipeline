"""
Application Configuration
Loads runtime configuration from .env
"""

from pathlib import Path
from dotenv import load_dotenv
import os

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

# ==========================================================
# Application
# ==========================================================

APP_NAME = os.getenv("APP_NAME", "Production Ingestion Pipeline")
APP_VERSION = os.getenv("APP_VERSION", "1.0.0")

# ==========================================================
# Logging
# ==========================================================

LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
LOG_DIRECTORY = BASE_DIR / os.getenv("LOG_DIRECTORY", "logs")

# ==========================================================
# Storage
# ==========================================================

OUTPUT_DIRECTORY = BASE_DIR / os.getenv("OUTPUT_DIRECTORY", "output")

# ==========================================================
# Chunking (Global Defaults)
# ==========================================================

CHUNK_SIZE = int(os.getenv("CHUNK_SIZE", 500))
CHUNK_OVERLAP = int(os.getenv("CHUNK_OVERLAP", 100))

# ==========================================================
# Source-Specific Chunking
# ==========================================================

PDF_CHUNK_SIZE = int(os.getenv("PDF_CHUNK_SIZE", CHUNK_SIZE))
PDF_CHUNK_OVERLAP = int(os.getenv("PDF_CHUNK_OVERLAP", CHUNK_OVERLAP))

WEB_CHUNK_SIZE = int(os.getenv("WEB_CHUNK_SIZE", CHUNK_SIZE))
WEB_CHUNK_OVERLAP = int(os.getenv("WEB_CHUNK_OVERLAP", CHUNK_OVERLAP))

CSV_CHUNK_SIZE = int(os.getenv("CSV_CHUNK_SIZE", CHUNK_SIZE))
CSV_CHUNK_OVERLAP = int(os.getenv("CSV_CHUNK_OVERLAP", 0))

JSON_CHUNK_SIZE = int(os.getenv("JSON_CHUNK_SIZE", CHUNK_SIZE))
JSON_CHUNK_OVERLAP = int(os.getenv("JSON_CHUNK_OVERLAP", 50))

# ==========================================================
# Filtering
# ==========================================================

MIN_CHUNK_LENGTH = int(os.getenv("MIN_CHUNK_LENGTH"))

# ==========================================================
# Supported Files
# ==========================================================

SUPPORTED_EXTENSIONS = [
    ext.strip()
    for ext in os.getenv(
        "SUPPORTED_EXTENSIONS",
        ".pdf,.csv,.json,.txt"
    ).split(",")
]

VECTOR_DB_DIRECTORY = BASE_DIR / os.getenv(
    "VECTOR_DB_DIRECTORY",
    "vector_db"
)

STORAGE_DIRECTORY = BASE_DIR / os.getenv(
    "STORAGE_DIRECTORY",
    "storage"
)

LOG_DIRECTORY.mkdir(exist_ok=True)
OUTPUT_DIRECTORY.mkdir(exist_ok=True)
VECTOR_DB_DIRECTORY.mkdir(exist_ok=True)
STORAGE_DIRECTORY.mkdir(exist_ok=True)

# ==========================================================
# Embeddings
# ==========================================================

EMBEDDING_MODEL = os.getenv(
    "EMBEDDING_MODEL",
    "sentence-transformers/all-MiniLM-L6-v2",
)

# ==========================================================
# Retrieval
# ==========================================================

RETRIEVAL_TOP_K = int(
    os.getenv("RETRIEVAL_TOP_K", 5)
)

# ==========================================================
# Reranker
# ==========================================================

RERANKER_MODEL = os.getenv(
    "RERANKER_MODEL",
    "cross-encoder/ms-marco-MiniLM-L-6-v2",
)

RERANK_TOP_K = int(
    os.getenv("RERANK_TOP_K", 5)
)


RETRIEVAL_CANDIDATES = int(
    os.getenv("RETRIEVAL_CANDIDATES", 20)
)

# ==========================================================
# Context Validation
# ==========================================================

MIN_CONTEXT_SCORE = float(
    os.getenv("MIN_CONTEXT_SCORE", 3.0)
)

# ==========================================================
# LLM Configuration
# ==========================================================

LLM_PROVIDER = os.getenv("LLM_PROVIDER", "groq")

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

GROQ_MODEL = os.getenv(
    "GROQ_MODEL",
    "llama-3.3-70b-versatile",
)