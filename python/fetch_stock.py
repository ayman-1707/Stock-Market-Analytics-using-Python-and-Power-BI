# import the libraries
import pandas as pd
import yfinance as yf
import os

# make a list of stock what all u want 
stocks = [
    "INFY.NS",         
    "HCLTECH.NS",      
    "SBIN.NS",        
    "HDFCBANK.NS",     
    "AXISBANK.NS",     
    "ICICIBANK.NS",    
    "HINDUNILVR.NS",   
    "ITC.NS",         
    "TRENT.NS",        
    "TATACONSUM.NS",   
    "TATAPOWER.NS",    
    "COALINDIA.NS",    
    "HINDALCO.NS",     
    "MCX.NS",          
    "BHARTIARTL.NS",   
    "TVSMOTOR.NS",    
    "TATAMOTORS.NS",   
    "CIPLA.NS",        
    "DRREDDY.NS",      
    "LUPIN.NS",        
    "SUNPHARMA.NS",    
    "BAJAJFINSV.NS",   
    "JIOFIN.NS",      
    "HDFCLIFE.NS",    
    "CHOLAFIN.NS",    
    "LT.NS",           
    "JSWSTEEL.NS",    
    "TATASTEEL.NS",   
    "TATACHEM.NS",     
    "INDIGOPNTS.NS"    
]


# fetch data using function
def fetch_stock(stock):
    print(f"\n Downloading {stock}.....")

    df = yf.download(
        stock,
        period="5y",
        interval="1d"
    )
    # skipping part if there is no data
    if df.empty:
        print(f"No data found for {stock}")
        return 
    
    # formating datset
    df =  df.reset_index()
    df.columns = df.columns.get_level_values(0)
    df.columns.name = None
    df["Date"] = pd.to_datetime(df["Date"])
    df["Date"] = df["Date"].dt.strftime("%d-%m-%Y")
    df = df[["Date", "Open", "High", "Low", "Close", "Volume"]]
    price_columns = ["Open", "High", "Low", "Close"]
    df[price_columns] = df[price_columns].round(2)
    df["Volume"] = (df["Volume"] / 100000).round(2)
    df.insert(0, "S.No", range(1, len(df) + 1))
    print(df.head())

# convert the dataframe to csv
    os.makedirs("Dataset",exist_ok=True)
    filename = f"Dataset/{stock.replace(".NS","")}.csv"
    df.to_csv(filename,index=False)
    print(f"{filename} saved successfully!!")

# use for loop 
for stock in stocks:
    fetch_stock(stock)


