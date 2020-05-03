import unittest
import sys
sys.path.append('../..')

from url import link_finder

BASE_URL = 'http://mock.org'
INPUT_FEED_WITH_ANCHOR_TAG = '''<a href="/check"</a>'''
INPUT_FEED_WITHOUT_ANCHOR_TAG = '''<head><body><p>"Hello"</p></body></head>'''

class TestUrlLinkFinder(unittest.TestCase):
    
    def setUp(self):
        self.link_finder = link_finder.LinkFinder(BASE_URL)
    
    def test_total_links_without_anchortag(self):
        self.link_finder.feed(INPUT_FEED_WITHOUT_ANCHOR_TAG)
        self.assertEqual(len(self.link_finder.get_links()), 0)

    def test_total_links_with_anchortag(self):
        self.link_finder.feed(INPUT_FEED_WITH_ANCHOR_TAG)
        self.assertEqual(len(self.link_finder.get_links()), 1)
    
if __name__ == '__main__':
    unittest.main(buffer=True)