from datetime import date
from application.http import http, urls
from application.db import db, models
from mongoengine import NotUniqueError


def get_single_day_history(ticker, date = str(date.today())):
    single_day_history_url = urls.world_trading_data_single_day_history(ticker, date)
    return http.get_json(single_day_history_url)


def store_single_day_history(ticker, date, single_day_history):
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
    history_url = urls.world_trading_data_full_history(ticker)
    return http.get_json(history_url)


def store_full_history(ticker, full_history):
    for date, single_day_history in full_history['history'].items():
        store_single_day_history(ticker, date, single_day_history)
