def nasdaq_large_cap_list():
    return "http://www.nasdaqomxnordic.com/aktier/listed-companies/nordic-large-cap"

def alpha_vantage_stock_price_history():
    return "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&outputsize=full&symbol={ticker}&apikey=SFZ2D9HYHGJNX02R"


def alpha_vantage_sma_history():
    return "https://www.alphavantage.co/query?function=SMA&symbol={ticker}&interval={interval}&time_period={time_period}&series_type=open&apikey=SFZ2D9HYHGJNX02R"