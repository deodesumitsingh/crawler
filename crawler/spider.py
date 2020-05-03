import logging

from urllib.request import Request, urlopen

from url.domain import get_domain_name
from url.link_finder import LinkFinder


class Spider:
    """
    Class is responsible for crawling a webapge.

    Attributes:
        base_url (str): Staring point of crawling.
        crawl_depth (int): Total depth upto which crawl works.
        domain_name (str): Domain name of the staring point.
        queue (list): List which consist of links yet to be crawled.
        crawled (set): Set of links which are crawled.
    """

    def __init__(self, url, depth):
        """
        Initializer of the Spider class.

        Parameters:
            url (str): Starting point crawling.
            depth (int): Total depth upto which crawler has to crawl.
        """

        self.base_url = url
        self.crawl_depth = depth
        self.domain_name = get_domain_name(url)
        self.queue = [url]  # to hold links yet to be crawl
        self.crawled = set()  # links that already crawled

    def crawl_page(self, depth):
        """
        Function responsible for crawling a page.

        Parameters:
            depth (int): Depth at which we have crawl.
        """

        logging.debug("Going to crawl pages at depth {}".format(depth))
        aux_queue = self.queue  # Aux queue which holds current queued URLs
        self.queue = []  # Reset queued container of object
        for page_url in aux_queue:
            print('Crawling.........')
            # Only process if it's not crawled
            if page_url not in self.crawled:
                page_links = self.gather_links(page_url)
                self.add_links_to_queue(page_links)
                self.crawled.add(page_url)

    def gather_links(self, page_url):
        """
        Function which will find all links present in the given web page.

        Parameters:
            page_url (str): Page who needs to cral to find links.

        Returns:
            set(): Represents all the links present in the specified URL.
        """

        html_string = ''
        try:
            logging.debug("Going to gather all links of page {}"
                          .format(page_url))
            page_header = get_headers()
            # Make the request to mimic as user-agent.
            # Most of the sites blocked crawled
            request = Request(url=page_url, headers=page_header)
            response = urlopen(request)
            # Skip static or JS file as they dosen't consist of
            # html tags.
            if 'text/html' in response.getheader('Content-Type'):
                # response consist of bytes
                # so we have to decode it further.
                html_bytes = response.read()
                html_string = html_bytes.decode('utf-8')
            # link_finder consists of all the links present
            # in the page_url
            link_finder = LinkFinder(self.base_url)
            # Feed will parse the html_string
            link_finder.feed(html_string)
            return link_finder.get_links()
        except Exception as e:
            logging.error("Error {} occured while gather links at url: {}"
                          .format(str(e), page_url))
        return set()

    def add_links_to_queue(self, links):
        """
        Add discorved URL's in page to queue.
        """
        for link in links:
            # If the link is already crawled or already present in
            # the queue no need to crawl it again.
            if (link in self.queue) or (link in self.crawled):
                continue
            # No need to enqueue those URL who has domain
            # different than base_url.
            if get_domain_name(link) != self.domain_name:
                continue
            self.queue.append(link)


def get_headers():
    """
    Function consist of header that mimic crawler as user-agent.

    Most of the site Forbidden crawler so add the header to crawler.
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) \
                       AppleWebKit/537.36 (KHTML, like Gecko) \
                       Chrome/41.0.2228.0 Safari/537.3'
    }
    return headers
