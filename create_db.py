import sqlite3
conn = sqlite3.connect('bank.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Customers (
    CustomerID INTEGER PRIMARY KEY,
    Name TEXT,
    Segment TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Transactions (
    TransactionID INTEGER PRIMARY KEY,
    CustomerID INTEGER,
    Amount REAL,
    Type TEXT,
    Date TEXT
)
''')

cursor.execute("INSERT INTO Customers VALUES (1, 'Alpha Corp', 'Corporate')")
cursor.execute("INSERT INTO Customers VALUES (2, 'Beta Ltd', 'Retail')")
cursor.execute("INSERT INTO Customers VALUES (3, 'Gamma Inc', 'Corporate')")

cursor.execute("INSERT INTO Transactions VALUES (101, 1, 50000, 'Credit', '2023-01-01')")
cursor.execute("INSERT INTO Transactions VALUES (102, 2, 1200, 'Debit', '2023-01-02')")
cursor.execute("INSERT INTO Transactions VALUES (103, 1, 100000, 'Credit', '2023-01-03')")
cursor.execute("INSERT INTO Transactions VALUES (104, 3, 300, 'Fee', '2023-01-04')")

conn.commit()
conn.close()
print("Bank Database Created Successfully: 'bank.db'")