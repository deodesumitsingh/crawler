from html.parser import HTMLParser
from urllib import parse


class LinkFinder(HTMLParser):
    """
    Class to holds links in a specified page

    Attributes:
        base_url (str): URL represents the startpoint of crawling.
        links (set): Container to hold found links
    """

    def __init__(self, base_url):
        """
        Initializer of LinkFinder as well of HTMLParser

        Parameters:
            base_url (str): URL respresetns the startpoint of crawling.
        """

        super().__init__()
        self.base_url = base_url
        self.links = set()

    def handle_starttag(self, tag, attrs):
        """Override of handle_starttag in HTMLParser"""

        if tag == 'a':  # Only have to process anchor tag
            for (attribute, value) in attrs:
                if attribute == 'href':  # href attr points to different url
                    # Most developer use relative path for link
                    # navigation. In order to crawl the relative path
                    # we have to join base_url.
                    url = parse.urljoin(self.base_url, value)
                    self.links.add(url)

    def get_links(self):
        """Returns all the links which is found in a web page"""

        return self.links
