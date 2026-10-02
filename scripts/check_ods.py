import duckdb

DB_PATH = "duckdb/superstore.duckdb"

con = duckdb.connect(DB_PATH)

print("Row count:")
print(
    con.execute("""
        SELECT COUNT(*)
        FROM ods.orders
    """).fetchone()[0]
)

print("\nColumns:")
print(
    con.execute("""
        DESCRIBE ods.orders
    """).fetchdf()
)

print("\nFirst 5 rows:")
print(
    con.execute("""
        SELECT *
        FROM ods.orders
        LIMIT 5
    """).fetchdf()
)

con.close()
