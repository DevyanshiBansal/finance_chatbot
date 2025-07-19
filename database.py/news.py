
import requests
import sqlite3
import time

API_KEY = "CD6Y2MLUEV865ZOM"
Tickers = [
    # # Indian companies
    "RELIANCE.NS", "TCS.NS", "INFY.NS", "HDFCBANK.NS", "ICICIBANK.NS",
    "SBIN.NS", "HINDUNILVR.NS", "BHARTIARTL.NS", "LT.NS", "TATAMOTORS.NS",
    # # US companies
    "AAPL", "GOOGL", "MSFT", "AMZN", "TSLA", "META", "NVDA", "JPM", "BRK.B", "JNJ"
]

conn = sqlite3.connect("finance_data1.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS financial_news(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ticker TEXT,
    headline TEXT,
    summary TEXT,
    datetime TEXT,
    Url TEXT
)
""")
conn.commit()

def fetch_and_store_news(symbol):
    url = f"https://www.alphavantage.co/query?function=NEWS_SENTIMENT&tickers={symbol}&apikey={API_KEY}"
    response = requests.get(url)
    data = response.json()
    

    news_items = data.get("feed",[])
    
    for item in news_items:
        headline = item.get("title","").strip()
        summary = item.get("summary","").strip()
        datetime_published = item.get("datetime_published","").strip()
        url_link = item.get("url","").strip()


        cursor.execute("""
        INSERT INTO financial_news (ticker, headline, summary, datetime, url)
        VALUES(?,?,?,?,?)
        """,(symbol,summary,datetime_published,url_link))
        conn.commit()


for ticker in Tickers:
    print(f"fetching news for {ticker}...")

    try:
        fetch_and_store_news(ticker)
    except Exception as e:
        print("Error with {ticker}",e)
    
    time.sleep(15)

conn.close()

      
