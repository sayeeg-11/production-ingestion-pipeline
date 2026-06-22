"""
Application Configuration
"""

from pathlib import Path

from dotenv import load_dotenv

import os

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

APP_NAME = os.getenv("APP_NAME")

APP_VERSION = os.getenv("APP_VERSION")

LOG_LEVEL = os.getenv("LOG_LEVEL")

LOG_DIRECTORY = BASE_DIR / os.getenv("LOG_DIRECTORY")

CHUNK_SIZE = int(os.getenv("CHUNK_SIZE"))

CHUNK_OVERLAP = int(os.getenv("CHUNK_OVERLAP"))

SUPPORTED_EXTENSIONS = os.getenv(
    "SUPPORTED_EXTENSIONS"
).split(",")