# 🕸️ Web Scrapper: Quotes to Scrape

A robust and clean Python-based Web Scraper designed for educational purposes. This project demonstrates the ability to navigate multi-page websites and extract data while maintaining high data integrity.

## 🛠️ Tech Stack & Features
- Python 3.x: Core logic.
- BeautifulSoup4 & Requests**: For HTML parsing and HTTP requests.
- CSV Handling: Implementing "utf-8-sig" encoding to ensure data is readable across all platforms (Excel, Pandas, etc.).
- Smart Page navigation: Automatically detects the "Next" button to scrape all available pages.
- Polite Scraping: Included "time.sleep()" to avoid server overloading.

## 📊 Extracted Data
The project successfully extracted 100 quotes, saved in "quotes_data.csv".
- Columns: Author & Quote.

## 🚀 How to Run
1. Clone the repo.
2. Install dependencies: "pip install requests beautifulsoup4" & "pip install requests".
3. Run: "python Quote_scrapper.py".
***Type what is in between the double quotes 👆👆👆 in your vs code or whatever you are using terminal or simply run the requirements using"pip install -r requirements.txt"***
---
*Developed as part of my learning path in Data Engineering & Robotics.* 🤖🦾
