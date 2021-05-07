"""Test path unit control"""

# Libraries
import unittest
from unittest.mock import patch

# Modules
from src.utils import path_utils


class TestPath(unittest.TestCase):
    """Test Class Path for Use of Files and directories"""
    @patch('os.listdir', return_value=['a', 'b', 'c'])
    def test_list_files_correctly(self, _):
        """Test of list files correctly"""
        self.assertEqual(
            path_utils.list_files('.'),
            ['a', 'b', 'c'],
            'Should list all files correctly'
        )
