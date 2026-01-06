import pandas as pd
print("----Starting ETL Process----")
df = pd.read_csv("trade_data.csv")
print("Raw Data Loaded.", len(df))

df = df.dropna(subset=['Ticker'])

df['Quantity'] = df['Quantity'].fillna(0)

df = df.drop_duplicates()

df['Tradevalue'] = df['Quantity'] * df['Price']

df.to_csv("clean_trades.csv", index=False)
print("Data cleaned and saved to 'clean_trades.csv'")
print(df)
