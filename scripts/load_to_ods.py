import duckdb

DB_PATH = "duckdb/superstore.duckdb"
CSV_PATH = "data/superstore.csv"

con = duckdb.connect(DB_PATH)

con.execute("CREATE SCHEMA IF NOT EXISTS ods")

con.execute("""
    CREATE OR REPLACE TABLE ods.orders AS
    SELECT *
    FROM read_csv_auto(?, header=True)
""", [CSV_PATH])

row_count = con.execute("""
    SELECT COUNT(*)
    FROM ods.orders
""").fetchone()[0]

print(f"Loaded {row_count} rows into ods.orders")

con.close()