import pandas as pd
from datetime import datetime
import sys

# Extract step
def extract(f_path):

    print("Start Extact.................")

    try :
        df = pd.read_csv(f_path)
        print("DONE Extract......................")
        return df
    except Exception as e:
        print("Extract error!!!!!!!!!!!!!")
        print(e)
        sys.exit(1)


# transform step 
def transform(df):
    print("Start Transform.................")

    try:
        df = df.drop_duplicates()
        df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")
        df["quantity"] = df["quantity"].fillna(1).astype(int)
        df["unit_price"] = df["unit_price"].fillna(0).astype(float)

        df["total_price"] = df["quantity"] * df["unit_price"]

        df["country"] = df["country"].str.upper()
        df["customer_name"] = df["customer_name"].str.title()

        

        print("DONE Transform")
        return df

    except Exception as e:
        print("Transform error!!!!!!!!!!!!!")
        print(e)
        sys.exit(1)

# LOAD step 

def load(df):
    print("START Load..............................")
    df.to_csv("output.csv", index=False)
    print(f"DONE Load to outputcsv.........")
# main

if __name__ == "__main__":

    start_time = datetime.now()
    print("START pipeline.........")
    data =  extract("data.csv")
    output = transform(data)
    load(output)
    end_time = datetime.now()

    print("ETL pipeline completed successfully")
    print("Time : ",  end_time - start_time)
