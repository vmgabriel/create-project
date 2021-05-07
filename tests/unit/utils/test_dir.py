"""Test Dir Utils"""

# Libraries
import unittest
from unittest.mock import patch
from pathlib import Path

# Modules
from src.utils import dir_utils


class TestDir(unittest.TestCase):
    """Test Dir Data Utils"""
    def setUp(self):
        self.directory = '~/test-repo'

    @patch('os.getcwd', return_value='/data')
    def test_pwd(self, _):
        """test pwd"""
        self.assertEqual(
            dir_utils.pwd(),
            '/data',
            'Should generate pwd route'
        )

    def test_format_with_slash_route(self):
        """
        test current route based into directories with slash
        """
        mock = '/data/1234/'
        self.assertEqual(
            dir_utils.format_route(mock),
            '/data/1234',
            'Should update format current route with slash'
        )

    def test_format_without_slash_route(self):
        """
        test current route based into directories without slash
        """
        mock = '/data/1234'
        self.assertEqual(
            dir_utils.format_route(mock),
            '/data/1234',
            'Should update format current route without slash'
        )

    def test_current_route(self):
        """test current route based into directories"""
        mock = '/data/1234/'
        self.assertEqual(
            dir_utils.current_route(mock),
            '/data/1234',
            'Should update current route - /data/1234/'
        )

    @patch('os.getcwd', return_value='/data')
    def test_current_without_first_slash_route(self, _):
        """test current route based into directories"""
        mock = 'data/1234/'
        self.assertEqual(
            dir_utils.current_route(mock),
            '/data',
            'Should update current without first slash and generate pwd'
        )

    def test_fiter_with_point_and_route(self):
        """test filter route, change state to route configuration"""
        mock = './data/1235'
        self.assertEqual(
            dir_utils.filter_route(mock),
            'data/1235',
            'Should filter data valid for route'
        )

    def test_filter_with_point_without_route(self):
        """test filter route . data start ''"""
        mock = '.'
        self.assertEqual(
            dir_utils.filter_route(mock),
            '',
            'Should filter without route'
        )

    def test_mkdir(self):
        """test mkdir -p using create directory"""
        path = '/a/b/c'
        with patch.object(Path, 'mkdir', return_value=True):
            self.assertEqual(
                dir_utils.mkdir(path),
                True,
                'Should mkdir'
            )

    @patch('os.getcwd', return_value='/data')
    def test_auto_complete_route_with_point(self, _):
        """test auto complete route with """
        mock = '.'
        self.assertEqual(
            dir_utils.auto_complete_route(mock),
            '/data',
            'Should auto complete route with data .'
        )

    @patch('os.getcwd', return_value='/data')
    def test_auto_complete_route_with_relative(self, _):
        """test auto complete route with """
        mock = 'a/b/c'
        self.assertEqual(
            dir_utils.auto_complete_route(mock),
            '/data/a/b/c',
            'Should auto complete route with data relative route'
        )

    @patch('os.getcwd', return_value='/data')
    def test_auto_complete_route_with_absolute(self, _):
        """test auto complete route with absolute"""
        mock = '/a/b/c'
        self.assertEqual(
            dir_utils.auto_complete_route(mock),
            '/a/b/c',
            'Should auto complete route with data absolute route'
        )

    @patch('os.getcwd', return_value='/data')
    def test_auto_complete_route_with_absolute_slach_end(self, _):
        """test auto complete route with absolute"""
        mock = '/a/b/c/'
        self.assertEqual(
            dir_utils.auto_complete_route(mock),
            '/a/b/c',
            'Should auto complete route with data absolute route slash end'
        )

    @patch('os.getcwd', return_value='/data')
    def test_auto_complete_route_with_absolute_slach_end_point_start(self, _):
        """test auto complete route with absolute"""
        mock = './a/b/c/'
        self.assertEqual(
            dir_utils.auto_complete_route(mock),
            '/data/a/b/c',
            'Should auto complete route with data absolute route with start slach'
        )

    def test_exist_dir_correctly(self):
        """test directory correctly"""
        self.assertEqual(
            dir_utils.exist('tests'),
            True,
            'Should exist correctly dir'
        )

    def test_exist_dir_error(self):
        """test directory error"""
        self.assertEqual(
            dir_utils.exist('/a/b/c'),
            False,
            'Should exist error dir'
        )
