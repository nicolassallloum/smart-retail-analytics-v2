import os
import pandas as pd
from sqlalchemy import create_engine, text

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "55432")
DB_NAME = os.getenv("DB_NAME", "smart_retail_dw")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "sra_password")

engine = create_engine(
    f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

def main():
    print("🚀 Starting Load to Postgres...")

    df = pd.read_csv("data/processed/sales_clean.csv")
    df["order_date"] = pd.to_datetime(df["order_date"])

    with engine.begin() as conn:

        print("🧹 Clearing tables...")
        conn.execute(text("TRUNCATE fact_sales CASCADE;"))
        conn.execute(text("TRUNCATE dim_product CASCADE;"))
        conn.execute(text("TRUNCATE dim_customer CASCADE;"))
        conn.execute(text("TRUNCATE dim_date CASCADE;"))

        # =====================
        # DIM DATE
        # =====================
        print("📅 Loading dim_date...")
        dim_date = df[["order_date"]].drop_duplicates()
        dim_date["date_key"] = dim_date["order_date"].dt.strftime("%Y%m%d").astype(int)
        dim_date["year"] = dim_date["order_date"].dt.year
        dim_date["month"] = dim_date["order_date"].dt.month
        dim_date["day"] = dim_date["order_date"].dt.day
        dim_date.rename(columns={"order_date": "full_date"}, inplace=True)

        dim_date.to_sql("dim_date", conn, if_exists="append", index=False)

        # =====================
        # DIM CUSTOMER
        # =====================
        print("👤 Loading dim_customer...")
        dim_customer = df[["customer_name", "city"]].drop_duplicates().reset_index(drop=True)
        dim_customer.to_sql("dim_customer", conn, if_exists="append", index=False)

        # =====================
        # DIM PRODUCT
        # =====================
        print("📦 Loading dim_product...")
        dim_product = df[["product_name", "category", "unit_price"]].drop_duplicates()
        dim_product.to_sql("dim_product", conn, if_exists="append", index=False)

        # =====================
        # FACT SALES
        # =====================
        print("📊 Loading fact_sales...")

        # Join keys
        df["date_key"] = df["order_date"].dt.strftime("%Y%m%d").astype(int)

        customer_lookup = pd.read_sql("SELECT customer_key, customer_name, city FROM dim_customer", conn)
        product_lookup = pd.read_sql("SELECT product_key, product_name, category FROM dim_product", conn)

        df = df.merge(customer_lookup, on=["customer_name", "city"])
        df = df.merge(product_lookup, on=["product_name", "category"])

        fact_sales = df[[
            "order_id",
            "date_key",
            "customer_key",
            "product_key",
            "quantity",
            "discount",
            "gross_amount",
            "net_amount",
            "payment_method",
            "is_returned"
        ]]

        fact_sales.to_sql("fact_sales", conn, if_exists="append", index=False)

    print("✅ Data Loaded Successfully!")

if __name__ == "__main__":
    main()