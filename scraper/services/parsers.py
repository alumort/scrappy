from bs4 import BeautifulSoup


class Parser:

    def parse(self, html):
        soup = BeautifulSoup(html, "html.parser")

        return soup.title.text