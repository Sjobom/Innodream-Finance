import urllib.request
import json

import requests


def get_json(url):
    with urllib.request.urlopen(url) as url_request:
        return json.loads(url_request.read().decode())


def get_html(url):
    response = requests.get(url)
    return response.text[:]
