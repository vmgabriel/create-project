"""Module Directory"""

# Libraries
import os


def pwd() -> str:
    """get a current directory"""
    return os.getcwd()


def filter_route(directory: str) -> str:
    """Select a path to process"""
    if directory == '.':
        return ''
    if directory[:2] == './':
        return directory[1:]
    return ''


def format_route(directory: str) -> str:
    """Format route data"""
    if directory[-1] == '/':
        return directory[:-1]
    return directory


def current_route(directory: str) -> str:
    """select of current route based into directory"""
    if directory[0] == '/':
        return format_route(directory)
    return pwd()
