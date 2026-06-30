# import libraries
import pandas as pd
import os

# creating a function to clean
def clean_stock(stock):
    print(f"\n cleaning {stock}.....")
    filename = f"Dataset/{stock}.csv"

    # if we find any file misses skip
    if not os .path.exists(filename):
        print(f"{filename} not found .skipping.... ")
        return
    
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

# if I copy name of comapnies from fetch_py there will be ns to avoid that ns 
# automatically cleaning every csv from Dataset folder
files =os.listdir("Dataset")

for file in files:
    if file.endswith(".csv"):
        stock = file.replace(".csv", "")
        clean_stock(stock)