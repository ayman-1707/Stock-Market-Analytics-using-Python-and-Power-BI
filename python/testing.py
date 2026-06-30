import yfinance as yf

df = yf.download("TATAMTRDVR.NS", period="5y")

# print(df.head())
print(df.empty)

# import yfinance as yf

# for ticker in ["SBIN.NS", "INFY.NS", "LT.NS"]:
#     df = yf.download(ticker, period="5y", progress=False)
#     print(ticker, "Empty:", df.empty)

# import yfinance as yf

# stock = yf.Ticker("TATAMOTORS.NS")
# df = stock.history(period="5y")

# print(df.head())
# print(df.empty)