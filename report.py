import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

conn = sqlite3.connect("database/sales.db")
df = pd.read_sql("""
SELECT Category, SUM(Sales) AS Revenue
FROM sales
GROUP BY Category
""", conn)

plt.bar(df["Category"], df["Revenue"])
plt.title("Revenue by Category")
plt.savefig("outputs/revenue_by_category.png")
plt.clf()

trend = pd.read_sql("""
SELECT Year, Month, SUM(Sales) AS Revenue
FROM sales
GROUP BY Year, Month
ORDER BY Year, Month
""", conn)
trend["Date"] = trend["Year"].astype(str) + "-" + trend["Month"].astype(str)
plt.plot(trend["Date"], trend["Revenue"])
plt.xticks(rotation=90)
plt.title("Monthly Sales Trend")
plt.tight_layout()
plt.savefig("outputs/monthly_trend.png")

conn.close()

print("Reports generated in outputs folder!")