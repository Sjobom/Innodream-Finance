from bs4 import BeautifulSoup

from app import http
from config import urls


def get_tickers_large_cap():
    tickers = list()
    url = urls.nasdaq_large_cap_list()
    html_string = http.get_html(url)
    soup = BeautifulSoup(html_string, 'lxml')
    table = soup.find_all('tbody')[0]

    for row in table.find_all('tr'):
        columns = row.find_all('td')
        if(columns[2].get_text() == "SEK"):
            tickers.append(columns[1].get_text())

    # format the tickers so that they work with alpha vantage
    # change space to dash and add Stockholm signature to the end of the tickers
    for i, ticker in enumerate(tickers):
        tickers[i] = tickers[i].replace(" ", "-")
        tickers[i] = tickers[i] + ".ST"

    return tickers

print(get_tickers_large_cap())