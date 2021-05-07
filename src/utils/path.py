"""Path Utils"""

# Libraries
import os
from typing import List


def list_files(directory: str) -> List[str]:
    """Get list of files and directories of one directory"""
    return os.listdir(directory)
