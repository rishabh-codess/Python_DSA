import csv
import sys
import requests
from bs4 import BeautifulSoup


def scrape_quotes(url: str) -> list[dict]:
    """Fetch and parse quote elements from the target webpage."""
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/120.0.0.0 Safari/537.36"
        )
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()  # Raises HTTPError for 4xx/5xx codes
    except requests.exceptions.RequestException as e:
        print(f"Network error while fetching {url}: {e}", file=sys.stderr)
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    quote_blocks = soup.find_all("div", class_="quote")

    extracted_data = []
    for block in quote_blocks:
        text_elem = block.find("span", class_="text")
        author_elem = block.find("small", class_="author")
        tag_elems = block.find_all("a", class_="tag")

        quote_text = text_elem.get_text(strip=True) if text_elem else ""
        author = author_elem.get_text(strip=True) if author_elem else "Unknown"
        tags = [t.get_text(strip=True) for t in tag_elems]

        extracted_data.append(
            {
                "quote": quote_text,
                "author": author,
                "tags": ", ".join(tags),
            }
        )

    return extracted_data


def save_to_csv(data: list[dict], filename: str = "quotes.csv") -> None:
    """Save extracted items to a CSV file."""
    if not data:
        print("No records found to save.")
        return

    keys = data[0].keys()
    with open(filename, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)

    print(f"Successfully saved {len(data)} items to '{filename}'.")


if __name__ == "__main__":
    target_url = "http://quotes.toscrape.com"
    print(f"Scraping data from {target_url}...")

    results = scrape_quotes(target_url)
    save_to_csv(results)