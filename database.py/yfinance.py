import sqlite3
import yfinance as yf
from datetime import datetime

# Step 1: Connect to SQLite database
conn = sqlite3.connect("finance_data1.db")
cursor = conn.cursor()

# Step 2: Create a table
cursor.execute("""
CREATE TABLE IF NOT EXISTS stock_prices (
    ticker TEXT,
    price REAL,
    date TEXT
)
""")
conn.commit()

# Step 3: Function to insert stock data
def insert_stock_price(data):
    cursor.execute("INSERT INTO stock_prices (ticker, price, date) VALUES (?, ?, ?)",
                   (data['ticker'], data['price'], data['date']))
    conn.commit()

# Step 4: Function to fetch latest stock price
def fetch_price(ticker):
    stock = yf.Ticker(ticker)
    data = stock.history(period="1d")
    if not data.empty:
        return {
            'ticker': ticker,
            'price': float(data['Close'].iloc[-1]),
            'date': datetime.today().strftime('%Y-%m-%d')
        }
    return None

# Step 5: Hardcoded ticker symbols (global)
tickers = [
    # US Stocks
    "AAPL", "GOOGL", "MSFT", "TSLA", "AMZN", "META", "NFLX", "NVDA", "JPM", "BRK-B",

    # Indian Stocks (NSE)
    "RELIANCE.NS", "TCS.NS", "INFY.NS", "ICICIBANK.NS", "HDFCBANK.NS", "SBIN.NS",

    # Indices
    "^NSEI", "^BSESN", "^DJI", "^GSPC", "^IXIC",

    # ETFs
    "SPY", "QQQ", "VTI", "IVV",

    # Cryptocurrencies
    "BTC-USD", "ETH-USD", "DOGE-USD",

    # Commodities
    "GC=F", "CL=F", "SI=F",

    # Forex
    "USDINR=X", "EURUSD=X", "JPY=X"
]

# Step 6: Loop through tickers and store data
for t in tickers:
    result = fetch_price(t)
    if result:
        insert_stock_price(result)
        print(f"Inserted data for {t}: {result}")
    else:
        print(f"Failed to fetch data for {t}")