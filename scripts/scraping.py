import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

BASE_URL = "https://books.toscrape.com/catalogue/"
START_URL = "https://books.toscrape.com/catalogue/page-1.html"
books = []

def scrape_page(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    for article in soup.select(".product_pod"):
        title = article.h3.a['title']
        price = article.select_one(".price_color").text.strip()
        availability = article.select_one(".availability").text.strip()
        rating = article.select_one('p.star-rating')['class'][1]
        image = "https://books.toscrape.com/" + article.img['src'].replace('../../', '')
        category = "unknown"  # opcional: simplificado para velocidade

        books.append({
            "title": title,
            "price": price,
            "availability": availability,
            "rating": rating,
            "category": category,
            "image": image
        })

    next_button = soup.select_one('li.next a')
    if next_button:
        next_page = "https://books.toscrape.com/catalogue/" + next_button['href']
        print(f"Going to next page: {next_page}")
        time.sleep(1)  # dá uma pausa de 1s pra não sobrecarregar o site
        scrape_page(next_page)

def main():
    print("Starting scraping...")
    scrape_page(START_URL)
    df = pd.DataFrame(books)
    df.to_csv('data/books.csv', index=False)
    print(f"Scraping finished. {len(books)} books saved to data/books.csv")

if __name__ == "__main__":
    main()
