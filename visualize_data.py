import sqlite3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

conn = sqlite3.connect('bank.db')

sql_command = '''
SELECT 
    c.Name,
    SUM(t.Amount) as Total_Volume
FROM Transactions t
JOIN Customers c ON t.CustomerID = c.CustomerID
GROUP BY c.Name
ORDER BY Total_Volume DESC
'''

df = pd.read_sql_query(sql_command, conn)
conn.close()

print("----Plotting Data----")
print(df)

plt.figure(figsize=(10,6))

plt.bar(df['Name'], df['Total_Volume'], color = 'skyblue')

plt.title("Total Transaction Volume by Client")
plt.xlabel("Client Name")
plt.ylabel("Volume ($)")
plt.grid(axis= 'y', linestyle = '--', alpha = 0.7)


plt.savefig('client_exposure_report.png')
print("Chart saved as 'client_exposure_report.png'")

