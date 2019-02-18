from application.http import http, urls

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
