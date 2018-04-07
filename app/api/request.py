from flask import Flask, jsonify, request
from app.finance import tickers

flask_app = Flask(__name__)


@flask_app.route('/tickers')
def get_tickers():
    ticker_dict = tickers.get_tickers_large_cap()
    return jsonify(ticker_dict)


