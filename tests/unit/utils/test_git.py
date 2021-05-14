"""Test Git Utils"""

# Libraries
import os
import unittest
from unittest.mock import patch, MagicMock
from git import Repo, GitCommandError, Git

# Modules
from src.utils import git_utils, dir_utils, path_utils


EXPECT_MESSAGE_REGEX_PERMISSION = """Cmd('git') failed due to: exit code(128)
  cmdline: git clone --branch=master -v {0} {1}
  stderr: 'fatal: could not create leading directories of '{1}': Permission denied
'"""


class TestGit(unittest.TestCase):
    """Git Genering Util Test"""
    repo = None

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

    def test_git_init_repository(self):
        """git init repository"""
        with patch('git.Repo') as MockRepo:
            MockRepo.return_value.init = self.repo
            repo = git_utils.init(self.correct_route)
            self.assertEqual(
                repo.__class__,
                Repo,
                'Should be Repo class'
            )

    def test_git_add_data_repository(self):
        """git add files of data repository"""
        new_file = dir_utils.join_path(
            self.correct_route,
            'other_data.txt'
        )
        path_utils.touch(new_file)

        with patch('git.cmd.Git') as MockRepo:
            MockRepo.return_value.add = self.repo
            repo = git_utils.add(self.repo, ['.'])
            self.assertEqual(
                repo.__class__,
                Repo,
                'Should be Repo add for repository'
            )

    @patch('src.utils.git.commit', return_value=None)
    def test_git_commit_repository(self, commit):
        """git commit files of data repository"""
        # Prepare
        commit = MagicMock(return_value=self.repo)
        message = 'repo status commit'
        other_correct = './test-r1'

        path_utils.rm(other_correct, is_dir=True)
        dir_utils.mkdir(other_correct)
        new_file = dir_utils.join_path(
            other_correct,
            'other_data.txt'
        )
        repo_int = git_utils.init(other_correct)
        path_utils.touch(new_file)
        repo_int = git_utils.add(repo_int, ['.'])

        # mocked_commit = git_utils
        # mocked_commit.commit = MagicMock(return_value=self.repo)
        data = commit(repo_int, message)
        self.assertEqual(
                data.__class__,
                self.repo.__class__,
                'Should be a repo commit'
            )
