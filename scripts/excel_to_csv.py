import pandas as pd

df = pd.read_excel("data/Superstore.xlsx")

df.to_csv(
    "data/superstore.csv",
    index=False
)

print("Rows:", len(df))
print("Columns:", len(df.columns))
print("Created: data/superstore.csv")