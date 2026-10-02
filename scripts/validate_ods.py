import duckdb

DB_PATH = "duckdb/superstore.duckdb"

con = duckdb.connect(DB_PATH)

print("1. Total rows:")
print(
    con.execute("""
        SELECT COUNT(*)
        FROM ods.orders
    """).fetchone()[0]
)

print("\n2. Unique Row IDs:")
print(
    con.execute("""
        SELECT COUNT(DISTINCT "Row ID")
        FROM ods.orders
    """).fetchone()[0]
)

print("\n3. Duplicate Row IDs:")
print(
    con.execute("""
        SELECT COUNT(*)
        FROM (
            SELECT "Row ID"
            FROM ods.orders
            GROUP BY "Row ID"
            HAVING COUNT(*) > 1
        )
    """).fetchone()[0]
)

print("\n4. Null values:")
print(
    con.execute("""
        SELECT
            SUM(CASE WHEN "Row ID" IS NULL THEN 1 ELSE 0 END) AS row_id_nulls,
            SUM(CASE WHEN "Order ID" IS NULL THEN 1 ELSE 0 END) AS order_id_nulls,
            SUM(CASE WHEN "Customer ID" IS NULL THEN 1 ELSE 0 END) AS customer_id_nulls,
            SUM(CASE WHEN "Product ID" IS NULL THEN 1 ELSE 0 END) AS product_id_nulls,
            SUM(CASE WHEN "Sales" IS NULL THEN 1 ELSE 0 END) AS sales_nulls,
            SUM(CASE WHEN "Quantity" IS NULL THEN 1 ELSE 0 END) AS quantity_nulls
        FROM ods.orders
    """).fetchdf()
)

con.close()