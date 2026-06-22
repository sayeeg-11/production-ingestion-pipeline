"""
File Utility Functions
"""

from pathlib import Path


def file_exists(path: str) -> bool:
    """
    Check if file exists.
    """

    return Path(path).exists()


def get_extension(path: str) -> str:
    """
    Returns file extension.
    """

    return Path(path).suffix.lower()


def create_directory(path: str):
    """
    Creates directory if absent.
    """

    Path(path).mkdir(
        parents=True,
        exist_ok=True,
    )