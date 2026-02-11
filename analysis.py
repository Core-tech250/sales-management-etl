import sqlite3
import pandas as pd

conn = sqlite3.connect("database/sales.db")

q1 = pd.read_sql("""
SELECT SUM(Sales) AS Total_Revenue
FROM sales
""", conn)

print("\nTotal Revenue:\n", q1)

q2 = pd.read_sql("""
SELECT Category, SUM(Sales) AS Revenue
FROM sales
GROUP BY Category
ORDER BY Revenue DESC
""", conn)

print("\nRevenue by Category:\n", q2)

q3 = pd.read_sql("""
SELECT City, SUM(Sales) AS Revenue
FROM sales
GROUP BY City
ORDER BY Revenue DESC
LIMIT 5
""", conn)

print("\nTop 5 Cities:\n", q3)


q4 = pd.read_sql("""
SELECT Year, Month, SUM(Sales) AS Monthly_Revenue
FROM sales
GROUP BY Year, Month
ORDER BY Year, Month
""", conn)

print("\nMonthly Trend:\n", q4.head())

conn.close()
