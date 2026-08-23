from .base import BaseScraper

class BookScraper(BaseScraper):
    def __init__(self):
        super().__init__("https://books.toscrape.com/")

    def scrape(self):
        soup = self._get_html()
        books = soup.select("article.product_pod")

        results = []

        for book in books:
            title = book.h3.a["title"]
            price = book.select_one(".price_color").text.strip()
            rating = book.select_one(".star-rating")["class"][1]

            results.append({
                "title": title,
                "price": price,
                "rating": rating,
            })

        return results
