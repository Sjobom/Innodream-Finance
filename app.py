from flask import Flask, jsonify, request
from application.finance import tickers
from application.util import config
from mongoengine import connect

if not config.secret_exists():
    print("No secret.json config file found (contains API key etc.)!\n"
          "Check the README for instructions on how to create one!")
    raise SystemExit


connect('innodream_finance')
flask_app = Flask(__name__, instance_path='/application/instance')
flask_app.config['JSON_AS_ASCII'] = False


@flask_app.route('/tickers')
def get_tickers():
    company_list = tickers.get_companies()
    company_ticker_json_dict = {'companies': company_list}
    return jsonify(company_ticker_json_dict)


