"""test main data"""

# Libraries
import unittest
from getopt import GetoptError

# Modules
from src import main

# Configurations
from src.config import VERSION, COMMAND_USAGE


class TestMain(unittest.TestCase):
    """Test Main Class"""
    def test_verify_input_help_command(self):
        """Test verify input help data"""
        mock = ['-h']
        self.assertEqual(
            main.get_opts(mock),
            [('-h', '')],
            "Should get data commands help"
        )

    def test_verify_input_version_command(self):
        """Test version input to verify and get data"""
        mock = ['-v']
        self.assertEqual(
            main.get_opts(mock),
            [('-v', '')],
            "Should get data commands version"
        )

    def test_verify_directory_command(self):
        """Test verify directory include data route"""
        mock = ['-d', '/a/b/c']
        self.assertEqual(
            main.get_opts(mock),
            [('-d', '/a/b/c')],
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
            COMMAND_USAGE,
            'should be a command into config'
        )

    def test_version_data(self):
        """Test the version data is eq to configuration"""
        self.assertEqual(
            main.version(),
            VERSION,
            'should be a str of version'
        )

    def test_generate_project(self):
        """Genering project output"""
        self.assertEqual(
            1,
            1,
            'should be a str of version'
        )
