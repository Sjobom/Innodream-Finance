from flask import Flask, jsonify, request
from application.finance import tickers
from application.util import config

if not config.secret_exists():
    print("No secret.json config file found (contains API key etc.)!\n"
          "Check the README for instructions on how to create one!")
    raise SystemExit



flask_app = Flask(__name__, instance_path='/application/instance')
flask_app.config['JSON_AS_ASCII'] = False


@flask_app.route('/tickers')
def get_tickers():
    ticker_dict = tickers.get_tickers_large_cap()
    ticker_json_dict = {'tickers':[]}
    for ticker, company_name in ticker_dict.items():
        ticker_json_dict['tickers'].append({'ticker':ticker, 'company_name':company_name})
    return jsonify(ticker_json_dict)


