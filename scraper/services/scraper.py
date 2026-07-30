import requests


class WebScraper:

    def fetch(self, url):
        response = requests.get(url)

        response.raise_for_status()

        return response.text