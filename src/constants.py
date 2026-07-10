"""
Application Constants
These values rarely change.
"""

# ==========================================================
# Application
# ==========================================================

APP_NAME = "Production Ingestion Pipeline"

APP_VERSION = "1.0.0"

# ==========================================================
# Files
# ==========================================================

LOG_FILE_NAME = "pipeline.log"

DEFAULT_ENCODING = "utf-8"

# ==========================================================
# Hashing
# ==========================================================

DEFAULT_HASH_ALGORITHM = "sha256"

# ==========================================================
# Source Names
# ==========================================================

SOURCE_PDF = "pdf"
SOURCE_CSV = "csv"
SOURCE_JSON = "json"
SOURCE_WEB = "web"

# ==========================================================
# Supported MIME Extensions
# ==========================================================

SUPPORTED_FILE_TYPES = [
    ".pdf",
    ".csv",
    ".json",
    ".txt",
]


VECTOR_DB_DIRECTORY = "vector_db"