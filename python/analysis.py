# import libraries
import pandas as pd
from datetime import datetime
import os

# KPI ANALYSIS
def analyse_stock(stock):
    print(f"\n analysing {stock}.....")
    filename = f"Cleaned_Dataset/{stock}.csv"
    # if we find any file misses skip
    if not os .path.exists(filename):
        print(f"{filename} not found .skipping.... ")
        return
    
    # read cleaned dataset of company
    df = pd.read_csv(filename)
    print(df.head())
    # getting the description of data and getting info about it
    print("\n Data Information")
    print(df.info())
    print("\n Data Statistical Summary")
    print(df.describe())

    # let's find KPI's
    print(f"Highest Open Price:₹{df['Open'].max()}")
    print(f"Average Open Price:₹{df['Open'].mean():.2f}")
    print(f"Lowest Open Price:₹{df['Open'].min()}")

    print(f"Highest High Price:₹{df['High'].max()}")
    print(f"Average High Price:₹{df['High'].mean():.2f}")
    print(f"Lowest High Price:₹{df['High'].min()}")

    print(f"Highest Low Price:₹{df['Low'].max()}")
    print(f"Average Low Price:₹{df['Low'].mean():.2f}")
    print(f"Lowest Low Price:₹{df['Low'].min()}")

    print(f"Highest Close Price:₹{df['Close'].max()}")
    print(f"Average Close Price:₹{df['Close'].mean():.2f}")
    print(f"Lowest Close Price:₹{df['Close'].min()}")

    print(f"Highest  Trading Volume Price:₹{df['Volume'].max()}")
    print(f"Average Trading Volume Price:₹{df['Volume'].mean():.2f}")
    print(f"Lowest Trading Volume Price:₹{df['Volume'].min()}")

    # MONTHLY ANALYSIS
    # Converting the Date
    df['Date'] = pd.to_datetime(df['Date'],format="%d-%m-%Y")
    # Creating Years
    df['Year'] = df['Date'].dt.year
    # Creating Months
    df['Month'] = df['Date'].dt.month_name()
    # And to Check the Result
    print(df[['Date','Year','Month']].head())
    # Now we group Year & Month
    Monthly_Analysis = (
    df.groupby(['Month','Year']).agg(
       {
           'Open':'mean',
           'High':'mean',
           'Low':'mean',
           'Close':'mean',
           'Volume':'mean'
       }
    )
    .reset_index()
    )

    # Now let's make Months in Order
    Month_Order = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]

    # ordering the Months to be in Order to Pandas
    Monthly_Analysis['Month'] = pd.Categorical(
        Monthly_Analysis['Month'],
        categories = Month_Order,
        ordered = True
    )

    # Sorting By Month And Then Year
    Monthly_Analysis = Monthly_Analysis.sort_values(
        ['Month','Year']
    )

    print(Monthly_Analysis)

    # Making a folder for Monthly Analysis
    os.makedirs("Analysed_Dataset",exist_ok=True)

    Monthly_Analysis.to_csv(
        f"Analysed_Dataset/{stock}_Monthly_Analysis.csv",
        index=False
    )

    print("Monthly_Analysis Saved Successfully")

# automatically analyse every csv from Dataset folder
files =os.listdir("Cleaned_Dataset")

for file in files:
    if file.endswith(".csv"):
     stock = file.replace(".csv", "")
     analyse_stock(stock)


