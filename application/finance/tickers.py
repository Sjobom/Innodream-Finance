from bs4 import BeautifulSoup
from application.http import http, urls
from application.db import db, models

def update_tickers():
    tickers = _crawl_stockholm_tickers()
    return _persist_tickers(tickers)


# returns dict with tickers and company name
def _crawl_stockholm_tickers():
    companies = list()
    url = urls.nasdaq_large_cap_list()
    html_string = http.get_html(url)
    soup = BeautifulSoup(html_string, 'lxml')
    table = soup.find_all('tbody')[0]

    for row in table.find_all('tr'):
        columns = row.find_all('td')
        if(columns[2].get_text() == "SEK"):
            company_name = columns[0].find_all('a')[0].get_text()
            ticker = _swedish_format(columns[1].get_text())
            companies.append({
                'ticker':ticker,
                'name': company_name
            })
    return companies


def _swedish_format(ticker):
    ticker = ticker.replace(" ", "-")
    ticker = ticker + ".ST"
    return ticker


def _persist_tickers(companies):
    for company in companies:
        ticker_document = models.Company(
            ticker=company['ticker'],
            name=company['name']
        )
        ticker_document.save()


def get_tickers():
    return models.Company.objects
