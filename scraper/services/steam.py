from .base import BaseScraper

class SteamScraper(BaseScraper):
    def __init__(self, search_term=""):
        super().__init__(f"https://store.steampowered.com/search/?term={search_term}")

    def scrape(self):
        soup = self._get_html()
        games = soup.select("a.search_result_row")

        results = []

        for game in games:
            title = game.select_one(".title").text.strip()

            price_tag = game.select_one(".search_price")
            price = price_tag.text.strip() if price_tag else "N/A"

            release_tag = game.select_one(".search_released")
            release_date = release_tag.text.strip() if release_tag else "N/A"

            results.append({
                "title": title,
                "price": price,
                "release_date": release_date,
            })

        return results