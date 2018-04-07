from bs4 import BeautifulSoup

from app import http
from config import urls
from app.db import queries
from app.db import db


def update_tickers_large_cap():
    tickers = get_tickers_large_cap()
    update_tickers(tickers)


def update_tickers(new_tickers):
    with db.connect() as conn:
        conn = db.connect()
        cur = conn.cursor()
        cur.execute(queries.get_all_tickers)
        tickers_from_db = cur.fetchall()
        tickers_from_db_dict = dict()
        for ticker_row in tickers_from_db:
            ticker = ticker_row[0]
            company_name = ticker_row[1]
            tickers_from_db_dict[ticker] = company_name
        for ticker, company_name in new_tickers.items():
            print(ticker)
            if ticker not in tickers_from_db_dict:
                print(company_name)
                cur.execute(queries.insert_ticker, (ticker, company_name))
        conn.commit()
        cur.close()


# returns dict with tickers and company name e.g {'ERIC-B.ST':'Ericsson', 'ABB.ST':'ABB', ...}
def get_tickers_large_cap():
    tickers = dict()
    url = urls.nasdaq_large_cap_list()
    html_string = http.get_html(url)
    soup = BeautifulSoup(html_string, 'lxml')
    table = soup.find_all('tbody')[0]

    for row in table.find_all('tr'):
        columns = row.find_all('td')
        if(columns[2].get_text() == "SEK"):
            company_name = columns[0].find_all('a')[0].get_text()
            ticker = format_ticker(columns[1].get_text())
            tickers[ticker] = company_name

    return tickers
# format the tickers so that they work with alpha vantage
# change space to dash and add Stockholm signature to the end of the tickers
def format_ticker(ticker):
    ticker = ticker.replace(" ", "-")
    ticker = ticker + ".ST"
    return ticker

update_tickers_large_cap()