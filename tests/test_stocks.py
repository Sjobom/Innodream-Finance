import unittest
from application.http import urls
from application.util import config
from application.finance import stock
from application.db import db


class TestStockMethods(unittest.TestCase):

    def test_single_day_history_url(self):
        url = urls.world_trading_data_single_day_history('ABB.ST', '2019-02-18')
        oracle = "https://www.worldtradingdata.com" \
                 "/api/v1/history_multi_single_day?symbol=ABB.ST&date=2019-02-18&api_token={token}"
        oracle = oracle.replace('{token}', config.get_stock_api_key())
        self.assertEqual(url, oracle)

    def test_single_day_history_response(self):
        oracle = {"date":"2019-02-15","data":{"ABB.ST":{"open":"180.00","close":"182.60","high":"183.55",
                                                        "low":"179.00","volume":"1958798"}}}
        json_response = stock.get_single_day_history('ABB.ST', '2019-02-15')
        self.assertDictEqual(json_response, oracle)

    def test_add_history_to_db(self):
        insert_result = stock.store_single_day_history('FAKE.ST', '1901-02-15',
                                                       {"open": "1337.00", "close": "1338.00", "high": "1340.00",
                                                        "low": "1330.00", "volume": "9000"})
        self.assertTrue(insert_result.acknowledged)
        mongo_db = db.get_mongo_db()
        delete_result = mongo_db.history.delete_one({'_id': insert_result.inserted_id})
        self.assertTrue(delete_result.acknowledged)
