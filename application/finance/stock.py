from datetime import date

from application.http import http, urls

def get_single_day_history(ticker, date = str(date.today())):
    single_day_history_url = urls.world_trading_data_single_day_history(ticker, date)
    return http.get_json(single_day_history_url)



