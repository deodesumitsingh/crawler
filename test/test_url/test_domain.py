import unittest
import sys
sys.path.append('../..')

from url import domain

VALID_URL = 'https://github.com'
INVALID_URL_1 = 'tel:+917205827364'
INVALID_URL_2 = '../check/status'
LONG_URL = 'https://help.github.com/lets/check/it/up'

class TestUrlDomain(unittest.TestCase):
    
    def test_get_domain_name_with_valid_url(self):
        domain_name = domain.get_domain_name(VALID_URL)
        self.assertEqual(domain_name, 'github.com')
    
    def test_get_domain_name_with_invalid_url(self):
        domain_name = domain.get_domain_name(INVALID_URL_1)
        self.assertEqual(domain_name, '')
        domain_name = domain.get_domain_name(INVALID_URL_2)
        self.assertEqual(domain_name, '')

    def test_get_sub_domain_name_with_url(self):
        url_netloc = domain.get_sub_domain_name(VALID_URL)
        self.assertEqual(url_netloc, 'github.com')
        url_netloc = domain.get_sub_domain_name(LONG_URL)
        self.assertEqual(url_netloc, 'help.github.com')
    
if __name__ == '__main__':
    unittest.main(buffer=True)