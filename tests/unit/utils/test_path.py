"""Test path unit control"""

# Libraries
import unittest
from unittest.mock import patch
from pathlib import Path

# Modules
from src.utils import path_utils, dir_utils


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

    @patch('os.remove', return_value=None)
    def test_rm_file(self, _):
        """test for remove file"""
        sep = path_utils.rm('data.txt')
        self.assertEqual(
            sep,
            True,
            'Should rm a file'
        )

    @patch('os.rmdir', return_value=None)
    def test_rm_directory(self, _):
        """test for remove directory"""
        route = './a'
        dir_utils.mkdir(route)
        sep = path_utils.rm('./a', is_dir=True)
        self.assertEqual(
            sep,
            True,
            'Should rm a directory'
        )

    @patch('pathlib.Path.touch', return_value=None)
    def test_touch_file(self, _):
        """test for touch file"""
        sep = path_utils.touch('./a.txt')
        self.assertEqual(
            sep,
            Path('./a.txt').touch(),
            'Should be file new for touch'
        )
