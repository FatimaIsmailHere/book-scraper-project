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

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv("C:/python3/pythonProject/books_detailed.csv")
sns.set(style="whitegrid")

plt.figure(figsize=(8,5))
sns.countplot(data=df, x="Rating", order=df["Rating"].value_counts().index, hue="Rating", palette="pastel", legend=False)

plt.title("Number of Books by Rating")
plt.xlabel("Rating")
plt.ylabel("Number of Books")
plt.tight_layout()
plt.show()

top_categories = df["Category"].value_counts().head(10)

plt.figure(figsize=(10,6))
top_categories.plot(kind="bar", color="skyblue")
plt.title("Top 10 Book Categories")
plt.ylabel("Number of Books")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

plt.figure(figsize=(8,5))
sns.boxplot(y=df["Price (£)"], color="lightgreen")
plt.title("Book Price Distribution")
plt.ylabel("Price (£)")
plt.tight_layout()
plt.show()

cheap_five_star = df[(df["Rating"] == "Five") & (df["Price (£)"] < 20)]
top_3 = cheap_five_star.sort_values("Price (£)").head(3)

print("Top 3 Cheapest 5-Star Books:")
print(top_3[["Title", "Price (£)", "Category", "Link"]])
