import sqlite3
import pandas as pd

conn = sqlite3.connect('bank.db')

sql_command = """
SELECT 
    c.Name,
    SUM(t.Amount) AS Total_Volume
FROM Transactions t
JOIN Customers c ON t.CustomerID = c.CustomerID
GROUP BY c.Name
"""
df = pd.read_sql(sql_command, conn)

print("----Query Results----")
print(df)

conn.close()