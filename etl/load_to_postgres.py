import os
import pandas as pd
from sqlalchemy import create_engine, text

def pg_url():
    return "postgresql+psycopg2://postgres:sra_password@localhost:55432/smart_retail_dw"
    # port = os.getenv("POSTGRES_PORT", "5432")
    # db = os.getenv("POSTGRES_DB", "smart_retail_dw")
    # user = os.getenv("POSTGRES_USER", "postgres")
    # pwd = os.getenv("POSTGRES_PASSWORD", "postgres")
    # return f"postgresql+psycopg2://{user}:{pwd}@{host}:{port}/{db}"

def main(clean_path="data/processed/sales_clean.csv"):
    engine = create_engine(pg_url())

    df = pd.read_csv(clean_path)
    df["order_date"] = pd.to_datetime(df["order_date"]).dt.date

    with engine.begin() as conn:
        # dims
        dim_date = pd.DataFrame({"full_date": sorted(df["order_date"].unique())})
        dim_date["year"] = pd.to_datetime(dim_date["full_date"]).dt.year
        dim_date["month"] = pd.to_datetime(dim_date["full_date"]).dt.month
        dim_date["day"] = pd.to_datetime(dim_date["full_date"]).dt.day
        dim_date["day_of_week"] = pd.to_datetime(dim_date["full_date"]).dt.day_name()
        dim_date["is_weekend"] = pd.to_datetime(dim_date["full_date"]).dt.weekday >= 5

        dim_customer = df[["customer_name", "city"]].drop_duplicates()
        dim_product = df[["product_name", "category"]].drop_duplicates()

        conn.execute(text("TRUNCATE fact_sales RESTART IDENTITY CASCADE;"))
        conn.execute(text("TRUNCATE dim_date RESTART IDENTITY CASCADE;"))
        conn.execute(text("TRUNCATE dim_customer RESTART IDENTITY CASCADE;"))
        conn.execute(text("TRUNCATE dim_product RESTART IDENTITY CASCADE;"))

        dim_date.to_sql("dim_date", conn, if_exists="append", index=False)
        dim_customer.to_sql("dim_customer", conn, if_exists="append", index=False)
        dim_product.to_sql("dim_product", conn, if_exists="append", index=False)

        # fetch ids for mapping
        date_map = pd.read_sql("SELECT date_id, full_date FROM dim_date", conn)
        cust_map = pd.read_sql("SELECT customer_id, customer_name, city FROM dim_customer", conn)
        prod_map = pd.read_sql("SELECT product_id, product_name, category FROM dim_product", conn)

        df2 = df.merge(date_map, left_on="order_date", right_on="full_date", how="left") \
                .merge(cust_map, on=["customer_name", "city"], how="left") \
                .merge(prod_map, on=["product_name", "category"], how="left")

        fact = df2[[
            "order_id",
            "date_id",
            "customer_id",
            "product_id",
            "quantity",
            "unit_price",
            "discount",
            "gross_amount",
            "net_amount",
            "payment_method",
            "is_returned"
        ]].rename(columns={"order_id": "order_ref"})

        fact.to_sql("fact_sales", conn, if_exists="append", index=False)

    print("? Loaded star schema into PostgreSQL:")
    print("- dim_date, dim_customer, dim_product, fact_sales")

if __name__ == "__main__":
    main()
