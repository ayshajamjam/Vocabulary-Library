import unittest
from urllib.request import urlopen
from bs4 import BeautifulSoup

# Integration Test


class Test(unittest.TestCase):
    bs = None  # Global Object shared between all tests

    def setUpClass():
        url = 'https://en.wikipedia.org/wiki/Python'
        Test.bs = BeautifulSoup(urlopen(url), 'html.parser')

    def test_titleText(self):
        pageTitle = Test.bs.find('h1').get_text()
        self.assertEqual('Python', pageTitle)

    def test_contentExists(self):
        content = Test.bs.find('div', {'id': 'mw-content-text'})
        self.assertIsNotNone(content)
