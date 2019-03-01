import unittest
from application.finance import tickers


class TestTickerMethods(unittest.TestCase):

    # TODO replace network call with mock
    def test_crawl_company_tickers(self):
        crawled_companies = tickers._crawl_stockholm_companies()
        self.assertTrue({'ticker':'ABB.ST', 'name': 'ABB Ltd'} in crawled_companies)
