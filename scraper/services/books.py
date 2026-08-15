from .base import BaseScraper

class BookScraper(BaseScraper):
    url = 'https://books.toscrape.com/'

scraper = BookScraper()

print(scraper.url)

soup = scraper._get_html()