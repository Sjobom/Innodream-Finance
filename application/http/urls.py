from application.util import config


def nasdaq_large_cap_list():
    return "http://www.nasdaqomxnordic.com/aktier/listed-companies/stockholm"


def world_trading_data_single_day_history(ticker, date):
    api_key = config.get_stock_api_key()
    url = "https://www.worldtradingdata.com/api/v1/history_multi_single_day?symbol={ticker}&date={date}&api_token={token}"
    url = url.replace("{ticker}", ticker)
    url = url.replace("{date}", date)
    url = url.replace("{token}", api_key)
    return url
