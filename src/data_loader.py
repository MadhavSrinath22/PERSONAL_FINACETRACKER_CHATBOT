import pandas as pd

def load_transactions(csv_path="transactions.csv"):
    df = pd.read_csv(csv_path)
    df['Date'] = pd.to_datetime(df['Date'])
    return df
