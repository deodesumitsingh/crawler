import logging

from urllib.parse import urlparse


def get_domain_name(url):
    """
    Function to return domain of a given url

    Parameters:
        url (str): URL of which domain name has to be extract.

    Returns:
        (str): Domain name of specified URL or empty string
    """
    try:
        # Consist of multiple CNAME in a given URL.
        # Example :- mail.google.com. Domain is google.com
        # For any valid URL last part is the domain name
        domain, extension = get_sub_domain_name(url).split('.')[-2:]
        return domain + '.' + extension
    except Exception as e:
        logging.error("Error {} happened for malformed url: {}"
                      .format(str(e), url))
    return ''


def get_sub_domain_name(url):
    """
    Function to return URI of the given URL.

    Parameters:
        url (str): URL whose URI has to be extract.

    Returns:
        (str): URI of the URL
    """
    return urlparse(url).netloc
