from config import urls
from app import http


# Request multiple SMA values for different amounts of data points between start and end
def get_multiple_sma_values(ticker, start, end):
    sma_dicts = dict()
    for time_period in range(start, end):
        print(str(time_period))
        sma_dicts[time_period] = get_sma_values(ticker, time_period, "daily")
    return sma_dicts


# Request SMA values from Alpha Vantage API
# interval = how often should the data points be (daily, weekly, monthly, 1min, 5min, 15min, 30min, 60min)
# time_period = how many data points should the sma use
def get_sma_values(ticker, time_period, interval):
    sma_dict = dict()
    sma_api_url = urls.alpha_vantage_sma_history()
    sma_api_url = sma_api_url.replace("{time_period}",str(time_period))
    sma_api_url = sma_api_url.replace("{ticker}", ticker)
    sma_api_url = sma_api_url.replace("{interval}", interval)
    data = http.get_json(sma_api_url)
    sma_json_dict = data["Technical Analysis: SMA"]
    for key, val in sma_json_dict.items():
        sma_dict[key] = val["SMA"]
    return sma_dict


# Compares SMA values to stock prices from a start date until now
# start_date = "2018-03-27" e.g.
# returns the percentage in revenue if you had bought and sold when the stock price and sma graphs intersected
def compare_sma_to_stock_price(smas, stock_prices, start_date):
    percent = 1
    stocks_owned = False
    buy_price = 0
    sell_price = 0
    for stock_date in sorted(smas):
        if stock_date > start_date:
            stock_price = float(stock_prices[stock_date])
            sma = float(smas[stock_date])
            if not stocks_owned and stock_price > sma and stock_price > 0.0: # TODO change behavior when stock value is zero
                stocks_owned = True
                buy_price = stock_price
            elif stocks_owned and sma > stock_price > 0.0:
                stocks_owned = False
                sell_price = stock_price
                revenue_factor = sell_price / buy_price
                percent = percent * revenue_factor

    return percent
