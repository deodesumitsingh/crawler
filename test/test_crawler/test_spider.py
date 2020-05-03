import unittest
import sys
sys.path.append('../..')

from crawler import spider

BASE_URL = 'https://github.com'
DEPTH = 1

class TestCrawlerSpider(unittest.TestCase):

    def setUp(self):
        self.spider = spider.Spider(BASE_URL, DEPTH)
    
    def test_spider_initialization(self):
        self.assertEqual(self.spider.base_url, BASE_URL)
        self.assertEqual(self.spider.crawl_depth, DEPTH)
        self.assertEqual(self.spider.domain_name, 'github.com')
        self.assertEqual(len(self.spider.queue), 1)
        self.assertEqual(len(self.spider.crawled), 0)
    
    def test_spider_crawl_page(self):
        self.spider.crawl_page(1)
        self.assertEqual(len(self.spider.crawled), 1)
        self.assertGreater(len(self.spider.queue), 1)

if __name__ == '__main__':
    unittest.main(buffer=True)