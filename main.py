import logging

from utils import argparser, logger, validators


def init():
    """
    Initialization of different component for application to run.

    It can consist of db/logging/networ, etc initilization.
    """
    logger.initialize()  # initializing logging


if __name__ == "__main__":
    """
    Entrypoint for the crawler.

    It does following thing in this manner:-
    1. Initializes different module like logging which is crucial \
       for applicaiton.
    2. Takes command line argument and validates it.
    3. Crawl the page but with check
    """
    init()
    logging.debug("\n" * 2)  # Keep subsquent logs seprated
    logging.debug("All initialization are successfull...")
    argument_parser = argparser.get_cmdline_parser()
    cmd_args = argument_parser.parse_args()
    validators.validate_cmd_args(cmd_args.url, cmd_args.depth)
