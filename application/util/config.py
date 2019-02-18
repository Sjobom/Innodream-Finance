from flask import  Flask
import os
import json

def get_db_config():
    secret = _get_secret_file()
    return secret['db']

def get_stock_api_key():
    secret = _get_secret_file()
    return secret['world_trading_data_api_key']

def _get_secret_file():
    app = Flask(__name__)
    file_name = os.path.join(app.instance_path, 'secret.json')
    try:
        with open(file_name) as secret_file:
            secret = json.load(secret_file)
            return secret
    except:
        return None

def secret_exists():
    return True if _get_secret_file() != None else False