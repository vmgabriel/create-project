"""Module of Control for usage of git"""

# Libraries
from git import Git, Repo


def clone(directory: str, repository: str, branch: str = 'master') -> Repo:
    """Clone Repository"""
    return Repo.clone_from(repository, directory, branch=branch)
