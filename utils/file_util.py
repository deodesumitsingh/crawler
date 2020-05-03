import logging
import sys

from os import makedirs
from os.path import abspath, dirname, isdir, join

CRAWLED_OUTPUT_DIRECTORY = 'output'
CRAWLED_FILE = 'crawled.txt'


def get_project_name(domain_name):
    """
    Function to get project name out of domain name.

    Project name is name of the domain without extension.

    Parameters:
        domain_name (str): Domain name of base URL.

    Results:
        (str): Domain name without extension.
    """

    if len(domain_name) < 1:
        logging.error("Domain {} is not valid. Exiting".format(domain_name))
        sys.exit(1)
    return domain_name.split('.')[0]


def get_project_directory(domain_name):
    """
    Function to returns the project directory.

    Parameters:
        domain_name (str): Domain name of base URL.

    Results:
        (str): Output directory of project present at same level of entrypoint.
    """
    project_name = get_project_name(domain_name)
    project_directory = join(dirname(dirname(abspath(__file__))),
                             CRAWLED_OUTPUT_DIRECTORY,
                             project_name)
    return project_directory


def get_project_crawled_file(domain_name):
    """
    Function to returns the crawled file of a project.

    Parameters:
        domain_name (str): Domain name of base URL.

    Returns:
        (str): Crawled file in directory /output/project_name/crawled.txt
    """

    project_directory = get_project_directory(domain_name)
    return join(project_directory, CRAWLED_FILE)


def is_project_already_crawled(domain_name):
    """
    Function to check whether a project is already crawled.

    Parameters:
        domain_name (str): Domain name of base URL.

    Returns:
        (bool): True if project is already crawled.
    """

    project_directory = get_project_directory(domain_name)
    return isdir(project_directory)


def crawled_links_to_file(domain_name, crawled_links):
    """
    Function to write crawled links to crawled_file

    Parameters:
        domain_name (str): Domain name of base URL.
        crawled_links (list): Lists those are all crawled.
    """

    # Create project directory before crawled_file
    make_project_directory(domain_name)
    project_crawled_file = get_project_crawled_file(domain_name)
    with open(project_crawled_file, 'w') as f:
        for link in crawled_links:
            f.write(link + '\n')


def make_project_directory(domain_name):
    """
    Function to make project directory in /output folder

    Parameters:
        domain_name (str): Domain name of base URL
    """

    makedirs(get_project_directory(domain_name))
