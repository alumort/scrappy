import requests
from bs4 import BeautifulSoup


class BaseScraper:
    def _get_html(self):
        requests.get()
        requests.raise_for_status()
        soup = BeautifulSoup()
        return soup
