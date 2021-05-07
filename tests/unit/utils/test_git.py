"""Test Git Utils"""

# Libraries
import os
import unittest
from unittest.mock import patch
from git import Repo, GitCommandError

# Modules
from src.utils import git_utils, dir_utils


EXPECT_MESSAGE_REGEX_PERMISSION = """Cmd('git') failed due to: exit code(128)
  cmdline: git clone --branch=master -v {0} {1}
  stderr: 'fatal: could not create leading directories of '{1}': Permission denied
'"""


class TestGit(unittest.TestCase):
    """Git Genering Util Test"""

    def setUp(self):
        """load data"""
        self.correct_route = '~/test-repo'
        self.correct_repository = 'https://github.com/vmgabriel/create-project.git'
        dir_utils.mkdir(self.correct_route)
        self.repo = Repo.init(self.correct_route)

    def test_git_clone_correctly(self):
        """git clone correctly test"""
        with patch.object(Repo, 'clone_from', return_value=self.repo):
            self.assertEqual(
                git_utils.clone(self.correct_route, self.correct_repository),
                self.repo,
                'Should git clone correctly'
            )

    def test_git_clone_error_permmission_path(self):
        """test git clone with error of path out this is based into route"""
        with self.assertRaises(GitCommandError):
            git_utils.clone('/a/b/c', self.correct_repository)

    def test_git_clone_error_permmission_repo(self):
        """test git clone with error of repo out this is based into route"""
        with self.assertRaises(GitCommandError):
            git_utils.clone(self.correct_route, 'github.com/vmgabriel/data.git')
