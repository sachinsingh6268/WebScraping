# 📚 BookScraper - Web Scraping Books by Category

This project is a web scraping app built in Python that extracts book information from the website [Books to Scrape](https://books.toscrape.com/). The scraper collects data **category-wise** and stores it in structured CSV files.

---

##  Features

- 🔍 Scrapes all **book categories** from the site
- 📁 Saves category names and their URLs in a `category_urls.csv` file
- 📦 For each category, extracts details of every book including:
  - Book title
  - Book URL
  - Price
  - Availability
  - Star rating
- 📊 Stores data category-wise in separate CSV files using `pandas`
- 🧼 Handles HTML parsing and data extraction using `BeautifulSoup`

---

## 🛠️ Tech Stack

- `Python 3.x`
- `requests` – for sending HTTP requests
- `BeautifulSoup` (`bs4`) – for parsing and extracting HTML content
- `pandas` – for tabular data handling and CSV export

---

## 📂 Folder Structure
```
├── data/
│   ├── input/
│   │    ├── Academic.html
│   │    ├── Art.html
│   │    ├── Business.html
│   │    └──...
│   └── output/
│        ├── book_category_urls.csv
│        ├── Academic.csv
│        ├── Art.csv
│        └──...
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
