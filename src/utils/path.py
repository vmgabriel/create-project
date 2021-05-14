"""Path Utils"""

# Libraries
import os
import shutil
from typing import List
from pathlib import Path


def list_files(directory: str) -> List[str]:
    """Get list of files and directories of one directory"""
    return os.listdir(directory)


def exist_file(route: str) -> bool:
    """Exist File Data Path"""
    return Path(route).exists()


def rm(directory: str, is_dir: bool = False) -> bool:
    """rm directory or file"""
    if not exist_file(directory):
        return True

    if is_dir:
        shutil.rmtree(directory)
    else:
        os.remove(directory)
    return True


def touch(file_route: str, exist_ok=True):
    """Touch a file"""
    return Path(file_route).touch(exist_ok=exist_ok)
