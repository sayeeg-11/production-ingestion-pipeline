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