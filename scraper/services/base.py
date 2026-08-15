import requests
from bs4 import BeautifulSoup
class BaseScraper:
    def _get_html(self):
        url = self.url
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, "html.parser")
        return soup
