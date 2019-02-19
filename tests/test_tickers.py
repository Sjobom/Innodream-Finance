import unittest
from application.finance import tickers


class TestTickerMethods(unittest.TestCase):

    def test_crawl_tickers(self):
        crawled_tickers = tickers._crawl_stockholm_tickers()
        self.assertTrue({'ticker':'ABB.ST', 'company_name': 'ABB Ltd'} in crawled_tickers)
