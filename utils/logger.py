import logging

from os.path import abspath, dirname, join

# Path specifies where crawler log has to be put.
# crawler.log is the file that consist of crawler's log and
# it is present at entry point of the program.
LOG_FILE_PATH = join(dirname(dirname(abspath(__file__))), 'crawler.log')

# Defines the format of the message in the LOG file
LOG_FORMAT = '%(asctime)s %(levelname)s %(filename)s:%(lineno)d - %(message)s'

# Date format which is used in the log file.
# 12-11-1994 00:12:12 date's format
LOG_DATE_FORMAT = r'%d-%m-%Y %H:%M:%S'

# Log level defines the logging to be done log of DEBUG level and above.
LOG_LEVEL = logging.DEBUG


def initialize():
    """
    Initializes logging modules which is used in crawler project
    """

    logging.basicConfig(filename=LOG_FILE_PATH,
                        format=LOG_FORMAT,
                        datefmt=LOG_DATE_FORMAT,
                        level=LOG_LEVEL)
