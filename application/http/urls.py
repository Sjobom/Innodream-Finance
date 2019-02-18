from application.util import config

def nasdaq_large_cap_list():
    return "http://www.nasdaqomxnordic.com/aktier/listed-companies/nordic-large-cap"

def alpha_vantage_stock_price_history():
    return "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&outputsize=full&symbol={ticker}&apikey=SFZ2D9HYHGJNX02R"


def alpha_vantage_sma_history():
    return "https://www.alphavantage.co/query?function=SMA&symbol={ticker}&interval={interval}&time_period={time_period}&series_type=open&apikey=SFZ2D9HYHGJNX02R"

def world_trading_data_single_day_history(ticker, date):
    api_key = config.get_stock_api_key()
    url = "https://www.worldtradingdata.com/api/v1/history_multi_single_day?symbol={ticker}&date={date}&api_token={token}"
    url = url.replace("{ticker}", ticker)
    url = url.replace("{date}", date)
    url = url.replace("{token}", api_key)
    return url
