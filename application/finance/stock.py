from datetime import date
from application.http import http, urls
from application.db import db, models
from mongoengine import NotUniqueError
from application.finance import tickers


def get_single_day_history(ticker, date = str(date.today())):
    single_day_history_url = urls.world_trading_data_single_day_history(ticker, date)
    single_day_history_json = http.get_json(single_day_history_url)
    if not contains_valid_data(single_day_history_json):
        return None
    return single_day_history_json


def store_single_day_history(ticker, date, single_day_history):
    if single_day_history is None:
        return
    history_document = models.History(
        ticker=ticker,
        date=date,
        open=single_day_history['open'],
        close=single_day_history['close'],
        high=single_day_history['high'],
        low=single_day_history['low'],
        volume=single_day_history['volume']
    )
    try:
        history_document.save()
    except NotUniqueError:
        pass  # we don't want duplicates, so this is ok!
    return history_document


def get_full_history(ticker):
    full_history_url = urls.world_trading_data_full_history(ticker)
    full_history_json = http.get_json(full_history_url)
    if not contains_valid_data(full_history_json):
        return None
    return full_history_json


def contains_valid_data(json):
    if 'Message' in json:
        print('invalid data found: ' + json['Message'])
        return False
    return True


def store_full_history(ticker, full_history):
    if full_history is None:
        return
    for date, single_day_history in full_history['history'].items():
        store_single_day_history(ticker, date, single_day_history)


def get_and_store_all_stockholm_stocks_full_history():
    stockholm_tickers = tickers.get_tickers()
    for ticker in stockholm_tickers:
        ticker_history = get_full_history(ticker['ticker'])
        store_full_history(ticker['ticker'], ticker_history)
