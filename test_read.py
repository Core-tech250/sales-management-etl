import pandas as pd

df = pd.read_csv("data/superstore.csv", encoding="latin1")

print("Rows:", df.shape[0])
print("Columns:", df.shape[1])
print("\nFirst 5 rows:\n")
print(df.head())