import pandas as pd
import sqlite3

print("Reading dataset...")
df = pd.read_csv("data/superstore.csv", encoding="latin1")

print("Initial shape:", df.shape)

print("\nCleaning data...")

df = df.drop_duplicates()

df['Order Date'] = pd.to_datetime(df['Order Date'])

df['Year'] = df['Order Date'].dt.year
df['Month'] = df['Order Date'].dt.month

df = df.dropna()

print("Cleaned shape:", df.shape)

print("\nLoading into database...")

conn = sqlite3.connect("database/sales.db")

df.to_sql("sales", conn, if_exists="replace", index=False)

conn.close()

print("Data successfully stored in database!")