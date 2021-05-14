"""Module Directory"""

# Libraries
import os
import pathlib


def pwd() -> str:
    """get a current directory"""
    return os.getcwd()


def filter_route(directory: str) -> str:
    """Select a path to process"""
    if directory == '.':
        return ''
    if directory[:2] == './':
        return directory[2:]
    return directory


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


def auto_complete_route(directory: str) -> str:
    """Route complete directory"""
    process = current_route(directory)
    if directory[0] != '/':
        route = filter_route(format_route(directory))
        with_route = f'/{route}' if route != '' else route
        process += with_route
    return process


def join_path(prev_path: str, curr_path: str):
    """include the path to prev_path"""
    return os.path.join(prev_path, curr_path)


def mkdir(path: str, exist_ok: bool = True) -> bool:
    """Create a directory"""
    pathlib.Path(path).mkdir(parents=True, exist_ok=exist_ok)
    return True


def exist(route: str) -> bool:
    """The dir exist?"""
    return os.path.exists(route)
