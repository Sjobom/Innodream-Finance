from bs4 import BeautifulSoup
from application.http import http, urls
from application.db import db, models


def update_tickers():
    companies = _crawl_stockholm_companies()
    return _persist_companies(companies)


# returns dict with tickers and company name
def _crawl_stockholm_companies():
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


def _persist_companies(companies):
    for company in companies:
        ticker_document = models.Company(
            ticker=company['ticker'],
            name=company['name']
        )
        ticker_document.save()


def get_companies():
    return models.Company.objects

def schedule_company_retrieval(scheduler):
    # update tickers every day
    scheduler.add_job(update_tickers, 'cron', hour=23, minute=0)