from bs4 import BeautifulSoup

from application.db import db
from application.db import queries
from application.http import http
from config import urls


def update_tickers_large_cap():
    tickers = _crawl_tickers_large_cap()
    _update_tickers(tickers)


def get_tickers_large_cap():
    tickers = dict()
    tickers_from_db = _get_tickers_from_db()
    for ticker_row in tickers_from_db:
        ticker = ticker_row[0]
        company_name = ticker_row[1]
        tickers[ticker] = company_name
    return tickers


def _update_tickers(new_tickers):
    with db.connect() as conn:
        cur = conn.cursor()
        tickers_from_db = _get_tickers_from_db()
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
def _crawl_tickers_large_cap():
    tickers = dict()
    url = urls.nasdaq_large_cap_list()
    html_string = http.get_html(url)
    soup = BeautifulSoup(html_string, 'lxml')
    table = soup.find_all('tbody')[0]

    for row in table.find_all('tr'):
        columns = row.find_all('td')
        if(columns[2].get_text() == "SEK"):
            company_name = columns[0].find_all('a')[0].get_text()
            ticker = _format_ticker(columns[1].get_text())
            tickers[ticker] = company_name

    return tickers


def _get_tickers_from_db():
    with db.connect() as conn:
        cur = conn.cursor()
        cur.execute(queries.get_all_tickers)
        tickers_from_db = cur.fetchall()
        return tickers_from_db

# format the tickers so that they work with alpha vantage
# change space to dash and add Stockholm signature to the end of the tickers
def _format_ticker(ticker):
    ticker = ticker.replace(" ", "-")
    ticker = ticker + ".ST"
    return ticker

update_tickers_large_cap()