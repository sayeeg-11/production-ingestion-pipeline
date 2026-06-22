"""
Central Logging Utility
"""

import logging

from pathlib import Path

from src.config import (
    LOG_DIRECTORY,
    LOG_LEVEL,
)

from src.constants import LOG_FILE_NAME


LOG_DIRECTORY.mkdir(
    parents=True,
    exist_ok=True,
)

log_path = Path(LOG_DIRECTORY) / LOG_FILE_NAME


logging.basicConfig(
    level=getattr(logging, LOG_LEVEL),
    format="%(asctime)s | %(levelname)s | %(message)s",
    handlers=[
        logging.FileHandler(log_path),
        logging.StreamHandler(),
    ],
)

logger = logging.getLogger("ingestion_pipeline")