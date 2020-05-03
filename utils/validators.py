import logging
import sys
import validators


def validate_cmd_args(url, depth):
    """
    Validates the command line parameter URL and Depth.

    It validates the URL and Depth as well checks whether the url already
    begin processed or not.

    Parameters:
        url (str): URL to be crawled
        depth (int): Depth upto which URL to be crawled.
    """
    invalid_parameter = False
    logging.debug("Going to validate URL: {} and Depth: {}".format(url, depth))
    if not validators.url(url):
        invalid_parameter = True
        print("Cannot process URL {} it not valid".format(url))
    if depth < 1:
        invalid_parameter = True
        msg = ("Cannot process request for URL {} because depth provided {}"
               " that should be greater than or equal to 1")
        print(msg.format(url, depth))
    if invalid_parameter:
        sys.exit(1)
