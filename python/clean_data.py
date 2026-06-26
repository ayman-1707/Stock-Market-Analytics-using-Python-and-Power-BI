# import libraries
import pandas as pd
import os

# create the same stock list without ns from fetch_data.py
stocks = [
    "CIPLA",
    "RELIANCE",
    "SBIN",
    "HDFCBANK",
    "ICICIBANK",
    "HINDUNILVR"
]

# creating a function to clean
def clean_stock(stock):
    print(f"\n cleaning {stock}.....")
    filename = f"Dataset/{stock}.csv"
    df = pd.read_csv(filename)
    print(df.head())
    print("\n Data Information")
    df.info()
    print("\nMissing Values")
    print(df.isnull().sum())
    print("\nDuplicate Rows")
    print(df.duplicated().sum())
    print("\nStatistical Summary")
    print(df.describe())
    os.makedirs("Cleaned_Dataset",exist_ok=True)
    cleaned_filename = f"Cleaned_Dataset/{stock}.csv"
    df.to_csv(cleaned_filename,index=False)
    print(f"{cleaned_filename} saved successfully!!")

# for loop 
for stock in stocks:
    clean_stock(stock)