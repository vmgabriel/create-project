"""Module of Control for usage of git"""

# Libraries
from typing import List
from git import Git, Repo


def clone(directory: str, repository: str, branch: str = 'master') -> Repo:
    """Clone Repository"""
    return Repo.clone_from(repository, directory, branch=branch)


def init(directory: str, mkdir: bool = False) -> Repo:
    """Initialize git Repository"""
    return Repo.init(directory, mkdir=mkdir)


def add(repo: Repo, files: List[str]) -> Repo:
    """add the files of list"""
    repo.git.add(files)
    return repo


def commit(repo: Repo, message: str) -> Repo:
    """commit the repo files status"""
    repo.git.commit(m=message)
    return repo
