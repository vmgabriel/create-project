"""All configuration"""

VERSION = '0.0.1'
COMMAND_NAME = 'init-project'

PYTHON_REPOSITORY = 'https://github.com/vmgabriel/python-base-project'
PYTHON_BRANCH = 'super'

COMMAND_USAGE = """{0}: the great project

usage: {0} [options] [language]

language: Support to all languages
  python: data value (default value)

Options:
  -d, --directory string  Location of directory to create a new project, for default .
  -h, --help              Print The Help
  -v, --version           Print Version Information an Quit

""".format(COMMAND_NAME)
