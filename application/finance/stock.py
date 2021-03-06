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
    stockholm_companies = tickers.get_companies()
    for company in stockholm_companies:
        ticker_history = get_full_history(company['ticker'])
        if ticker_history is None:
            return
        store_full_history(company['ticker'], ticker_history)


def get_and_store_all_stockholm_stocks_day_history(date):
    stockholm_companies = tickers.get_companies()
    for company in stockholm_companies:
        ticker_history = get_single_day_history(company['ticker'], date)
        if ticker_history is None:
            return
        store_single_day_history(company['ticker'], date, ticker_history['data'][company['ticker']])


def schedule_stock_retrieval(scheduler):
    # get day history every weekday
    scheduler.add_job(func=get_and_store_all_stockholm_stocks_day_history, args=[str(date.today())], trigger='cron', day_of_week='mon-fri', hour=0, minute=0)
    # get full history every sunday (if something went wrong earlier)
    scheduler.add_job(get_and_store_all_stockholm_stocks_full_history, 'cron', day_of_week='sun', hour=0, minute=0)
