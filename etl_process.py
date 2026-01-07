import pandas as pd
import numpy as np
print("----Starting ETL process----")
df = pd.read_csv("trade_data.csv")
print("Raw data loaded", len(df))

df = df.dropna(subset=['Ticker'])

df = df.fillna(0)

df = df.drop_duplicates()

df['trade_value'] = df['Quantity'] * df['Price']

df['Risk_Level'] = np.where(df['trade_value'] > 5000, 'High', 'Low')
print("Risk Classification complete")

df.to_csv('clean_trades.csv')