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
