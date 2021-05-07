"""Application Base"""

# Libraries
from typing import List, Tuple
import sys
from getopt import getopt, GetoptError

# Configurations
from src.config import VERSION, COMMAND_USAGE
from src.utils import dir_utils

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


def get_opts(argv: List[str]) -> List[Opts]:
    """
    Verify and get opts for de argv of input

    This can generate a GetoptError Exception - with option not recognized
    """
    try:
        opts, _ = getopt(
            argv,
            COMMAND_ABBREV,
            COMMAND_POSIBILITIES
        )
        return opts
    except GetoptError as exc:
        raise exc


def generate_project(directory: str = '.') -> str:
    """Generate project based into directory"""
    new_path = dir_utils.auto_complete_route(directory)
    print(new_path)
    print(dir_utils.pwd())
    return directory


def define_output(opts: List[Opts]) -> str:
    """
    Define the output based into opts

    This can generate a Exception Error based into unhnadled option
    """
    if len(opts) == 0:
        return generate_project()

    _o, _a = opts[0]
    if _o in ('-v', '--version'):
        return version()
    if _o in ('-h', '--help'):
        return usage()

    if _o in ('-d', '--directory'):
        # With directory Directory
        return generate_project(_a)
    return generate_project()


def load_script():
    """Load the script data"""
    try:
        opts = get_opts(sys.argv[1:])
        define_output(opts)
        sys.exit()
    except Exception as exc:
        print('[Error] - ', exc)
        sys.exit(2)
