from datetime import date
from application.http import http, urls
from application.db import db

def get_single_day_history(ticker, date = str(date.today())):
    single_day_history_url = urls.world_trading_data_single_day_history(ticker, date)
    return http.get_json(single_day_history_url)

def store_single_day_history(ticker, date, history):
    mongo_db = db.get_mongo_db()
    history_data = {
        'ticker': ticker,
        'date': date,
        'history': history
    }
    return mongo_db.history.insert_one(history_data)






