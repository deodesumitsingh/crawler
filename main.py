import logging
import sys

from crawler.spider import Spider
from url.domain import get_domain_name
from utils import argparser, logger, file_util, validators


def start_crawling(url, depths):
    """
    Function that is responsible from crawling the specified url.

    Parameters:
        url (str): Base URL which has to be crawled.
        depths (int): Depth upto which base URL has to be crawled.
    """

    domain_name = get_domain_name(url)
    if len(domain_name) == 0:
        print("Domain {} for Url {} is not valide. Cannot proceed further"
              .format(domain_name, url))
        sys.exit(1)

    if file_util.is_project_already_crawled(domain_name):
        print("Url {} already crawled checked inside /output/{}/crawled.txt"
              .format(url, file_util.get_project_name(domain_name)))
        sys.exit(1)

    spider = Spider(url, depths)

    for depth in range(1, depths + 1):
        if len(spider.queue) > 0:
            print("Crawling started at depth {}".format(depth))
            spider.crawl_page(depth)
        else:
            print("No new links to crawl at depth {}. Stopping crawl"
                  .format(depth))
            break
    file_util.crawled_links_to_file(domain_name, spider.crawled)
    print_msg = ("\n\nCrawling is completed for URL {}.\n"
                 "Please check the crawled file at {}/crawled.txt\n")
    print(print_msg.format(url, file_util.get_project_directory(domain_name)))


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
    start_crawling(cmd_args.url, cmd_args.depth)
