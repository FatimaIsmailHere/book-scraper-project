# book-scraper-project
A Python web scraping and data analysis project using books.toscrape.com
# Book Scraper & Analyzer

This project scrapes data from [books.toscrape.com](http://books.toscrape.com), then analyzes and visualizes it using Python.

# Features:
- Scrapes title, price, rating, availability, category, and link
- Works across all pages
- Saves data to `books_detailed.csv`
- Creates visualizations with Seaborn & Matplotlib

# Visualizations
- Number of books by rating
- Top 10 categories
- Price distribution
- Cheapest 5-star books

# How to Run
1. Clone this repo
2. Run `book_scraper.py`
3. Open `analysis_visuals.ipynb` for charts

# Requirements
- requests
- beautifulsoup4
- pandas
- matplotlib
- seaborn
