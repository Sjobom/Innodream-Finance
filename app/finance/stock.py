from config import urls
from app import http

# Request the closing stock price history for a specific stock ticker
def get_stock_price_close_history(ticker):
    stock_price_dict = dict()
    daily_stock_price_api_url = urls.alpha_vantage_stock_price_history()
    daily_stock_price_api_url = daily_stock_price_api_url.replace("{ticker}", ticker)
    data = http.get_json(daily_stock_price_api_url)
    stock_price_json_dict = data["Time Series (Daily)"]
    for key, val in stock_price_json_dict.items():
        stock_price_dict[key] = val["4. close"]
    return stock_price_dict
