"""Application Base"""

# Libraries
from typing import List, Tuple
import sys
from getopt import getopt, GetoptError

# Configurations
from src.config import (
    VERSION,
    COMMAND_USAGE,
    PYTHON_REPOSITORY,
    PYTHON_BRANCH
)
from src.utils import dir_utils, git_utils, path_utils

# Constants
COMMAND_ABBREV = "hd:v"
COMMAND_POSIBILITIES = ['help', 'directory=', 'version']

Opts = Tuple[str, str]


def version():
    """The Version of command"""
    print(VERSION)
    return VERSION


def usage():
    """This explain the usage of command"""
    print(COMMAND_USAGE)
    return COMMAND_USAGE


def get_repository(args: str) -> (str, str):
    """
    Get Repository and branch

    this can generate exception error based into not valid language
    """
    if args is None:
        return PYTHON_REPOSITORY, PYTHON_BRANCH

    args = args.strip().lower()
    if args in ('python', ''):
        return PYTHON_REPOSITORY, PYTHON_BRANCH
    raise Exception('Not Valid Language')


def get_opts(argv: List[str]) -> (List[Opts], List[str]):
    """
    Verify and get opts for de argv of input

    This can generate a GetoptError Exception - with option not recognized
    """
    try:
        return getopt(
            argv,
            COMMAND_ABBREV,
            COMMAND_POSIBILITIES
        )
    except GetoptError as exc:
        raise exc


def generate_project(args: List[str], directory: str = '.') -> bool:
    """
    Generate project based into directory

    this can generate Exception error if not is valid language
    """
    try:
        # Create new path
        new_path = dir_utils.auto_complete_route(directory)
        if not dir_utils.exist(new_path):
            dir_utils.mkdir(new_path)

        # generate repository
        arg_data = args[0] if len(args) > 0 else ''
        repository, branch = get_repository(arg_data)

        # clone repository
        git_utils.clone(new_path, repository, branch)

        # remove git path
        git_path = dir_utils.join_path(new_path, '.git')
        path_utils.rm(git_path, is_dir=True)

        # Initialize new git repository
        repo = git_utils.init(new_path)

        # commit to actual data
        repo = git_utils.add(repo, ['.'])
        repo = git_utils.commit(repo, message='feat: include commit')

        return len(path_utils.list_files(new_path)) > 0
    except Exception as exc:
        raise exc


def define_output(opts: List[Opts], args: List[str]) -> str:
    """
    Define the output based into opts

    This can generate a Exception Error based into unhnadled option,
    too can generate Exception error if language is not valid or not supported
    """
    try:
        if len(opts) == 0:
            return generate_project(args)

        _o, _a = opts[0]
        if _o in ('-v', '--version'):
            return version()
        if _o in ('-h', '--help'):
            return usage()

        if _o in ('-d', '--directory'):
            return generate_project(args, _a)
        return generate_project(args)
    except Exception as exc:
        raise exc


def load_script():
    """Load the script data"""
    try:
        opts, args = get_opts(sys.argv[1:])
        define_output(opts, args)
        sys.exit()
    except Exception as exc:
        print('[Error] - ', exc)
        sys.exit(2)
