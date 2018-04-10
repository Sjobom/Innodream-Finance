from application.finance import sma
from application.finance import stock

sma_values = sma.get_sma_values("ABB.ST", 10, "daily")
stock_prices = stock.get_stock_price_close_history("ABB.ST")
percent = sma.compare_sma_to_stock_price(sma, stock_prices, "2017-05-02")
print(percent)