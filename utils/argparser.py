import argparse

PROJECT_DESCRIPTION = 'Program to crawl a given website with specified depth'
PROJECT_EPILOG = 'Enjoy the crawler :)'

URL_HELP_MSG = 'URL to be crawled'
DEPTH_HELP_MSG = 'Upto which DEPTH specified URL to be crawled'


def get_cmdline_parser():
    """
    Function to return ArgumentParser for command line parsing.

    Returns:
        argument_parser (argparser.ArgumentParser): parser for command line URL
                                                    and Depth parameter.
    """
    argument_parser = argparse.ArgumentParser(description=PROJECT_DESCRIPTION,
                                              epilog=PROJECT_EPILOG)
    # Add url argument which takes the URL to be crawled
    argument_parser.add_argument('-u',
                                 '--url',
                                 action='store',
                                 type=str,
                                 required=True,
                                 help=URL_HELP_MSG)
    # Add depth argument which takes the above URL and
    # traverse it upto specified depth.
    argument_parser.add_argument('-d',
                                 '--depth',
                                 action='store',
                                 type=int,
                                 required=True,
                                 help=DEPTH_HELP_MSG)

    return argument_parser
