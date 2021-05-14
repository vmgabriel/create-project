"""test main data"""

# Libraries
import unittest
from unittest.mock import patch
from getopt import GetoptError

# Modules
from src import main, config


class TestMain(unittest.TestCase):
    """Test Main Class"""
    def test_verify_input_help_command(self):
        """Test verify input help data"""
        mock = ['-h']
        self.assertEqual(
            main.get_opts(mock),
            ([('-h', '')], []),
            "Should get data commands help"
        )

    def test_verify_input_version_command(self):
        """Test version input to verify and get data"""
        mock = ['-v']
        self.assertEqual(
            main.get_opts(mock),
            ([('-v', '')], []),
            "Should get data commands version"
        )

    def test_verify_directory_command(self):
        """Test verify directory include data route"""
        mock = ['-d', '/a/b/c', 'python']
        self.assertEqual(
            main.get_opts(mock),
            ([('-d', '/a/b/c')], ['python']),
            "Should get data commands version"
        )

    def test_verify_error_command(self):
        """Test verify error data command state not use"""
        mock = ['-s']
        with self.assertRaises(GetoptError):
            main.get_opts(mock)

    def test_verify_error_message_command(self):
        """Test verify error data command state not use"""
        mock = ['-s']
        with self.assertRaisesRegex(GetoptError, 'option -s not recognized'):
            main.get_opts(mock)

    def test_usage_data(self):
        """Test the usage data is eq to configuration"""
        self.assertEqual(
            main.usage(),
            config.COMMAND_USAGE,
            'should be a command into config'
        )

    def test_version_data(self):
        """Test the version data is eq to configuration"""
        self.assertEqual(
            main.version(),
            config.VERSION,
            'should be a str of version'
        )

    def test_generate_repository(self):
        """Test for generate a repository data"""
        sep = main.get_repository('')
        mock_repository = (config.PYTHON_REPOSITORY, config.PYTHON_BRANCH)
        self.assertEqual(
            sep,
            mock_repository,
            'should be a repository valid for "" value'
        )
        sep = main.get_repository('python')
        mock_repository = (config.PYTHON_REPOSITORY, config.PYTHON_BRANCH)
        self.assertEqual(
            sep,
            mock_repository,
            'should be a repository valid for "python" value'
        )

        sep = main.get_repository(None)
        mock_repository = (config.PYTHON_REPOSITORY, config.PYTHON_BRANCH)
        self.assertEqual(
            sep,
            mock_repository,
            'should be a repository valid for None value'
        )

        with self.assertRaisesRegex(Exception, 'Not Valid Language'):
            main.get_repository('smalltalk')

    @patch('src.utils.git_utils.commit', return_value=None)
    @patch('src.utils.git_utils.clone', return_value=None)
    @patch('os.rmdir', return_value=None)
    def test_generate_project_correctly(self, *args):
        """Genering project output correctly"""
        mock = './test-rm'
        self.assertEqual(
            main.generate_project([], mock),
            True,
            'should generate a project correctly'
        )
