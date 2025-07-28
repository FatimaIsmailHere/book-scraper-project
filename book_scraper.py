import requests
from bs4 import BeautifulSoup
import pandas as pd

base_url = "http://books.toscrape.com/"
page_url = "http://books.toscrape.com/catalogue/page-1.html"

all_books = []

while True:
    data = requests.get(page_url)
    data.encoding = "utf-8"
    cleandata = BeautifulSoup(data.text, "html.parser")

    books = cleandata.select("article.product_pod")

    for book in books:
        title = book.h3.a["title"]

        price_text = book.select_one(".price_color").text.strip()
        price = price_text.replace("£", "").replace("Â", "").strip()

        rating_tag = book.find("p", class_="star-rating")
        rating = rating_tag.get("class", [None, "Not Rated"])[1]


        availability = book.select_one(".availability").text.strip()


        link = book.h3.a["href"].replace("../../../", "")
        full_link = base_url + "catalogue/" + link


        book_page = requests.get(full_link)
        book_soup = BeautifulSoup(book_page.text, "html.parser")
        category = book_soup.select("ul.breadcrumb li a")[2].text.strip()

        all_books.append({
            "Title": title,
            "Price (£)": float(price),
            "Rating": rating,
            "Availability": availability,
            "Category": category,
            "Link": full_link
        })


    next_button = cleandata.select_one("li.next > a")
    if next_button:
        next_href = next_button["href"]
        page_url = base_url + "catalogue/" + next_href
    else:
        break

df = pd.DataFrame(all_books)
df.to_csv("books_detailed.csv", index=False)
print("Done! All books saved in books_detailed.csv")

