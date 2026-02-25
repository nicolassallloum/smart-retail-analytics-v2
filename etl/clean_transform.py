import os
import re
import pandas as pd
import numpy as np
from dateutil import parser

CITY_MAP = {
    "beirut": "Beirut",
    "beirut ": "Beirut",
    " ?????": "Beirut",
    "?????": "Beirut",
}

def parse_date_safe(x: str):
    try:
        return parser.parse(str(x), dayfirst=True).date()
    except Exception:
        return None

def normalize_city(x: str) -> str:
    if x is None:
        return None
    x2 = str(x).strip()
    key = x2.lower()
    return CITY_MAP.get(key, x2)

def clean_price(x):
    if pd.isna(x):
        return None
    s = str(x).strip()
    s = s.replace("$", "")
    s = s.replace(",", ".")
    s = re.sub(r"[^\d\.]", "", s)
    try:
        return float(s)
    except Exception:
        return None

def main(in_path="data/raw/sales_raw.csv", out_path="data/processed/sales_clean.csv"):
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    df = pd.read_csv(in_path)

    before = len(df)

    # dates
    df["order_date_parsed"] = df["order_date"].apply(parse_date_safe)

    # strings
    df["customer_name"] = df["customer_name"].astype(str).str.strip().str.title()
    df["city"] = df["city"].apply(normalize_city)

    # numeric
    df["unit_price_num"] = df["unit_price"].apply(clean_price)
    df["quantity"] = pd.to_numeric(df["quantity"], errors="coerce")
    df["discount"] = pd.to_numeric(df["discount"], errors="coerce")

    df["quantity"] = df["quantity"].fillna(1).clip(lower=1)
    df["discount"] = df["discount"].fillna(0).clip(lower=0)

    # business metrics
    df["gross_amount"] = (df["unit_price_num"] * df["quantity"]).round(2)
    df["net_amount"] = (df["gross_amount"] - df["discount"]).round(2)
    df["is_returned"] = df["returned"].astype(str).str.upper().eq("Y")

    # quality rules
    df = df.dropna(subset=["order_date_parsed", "unit_price_num", "product_name", "category", "city"])
    df = df[df["unit_price_num"] > 0]
    df = df[df["net_amount"] >= 0]

    after = len(df)

    out = df[[
        "order_id",
        "order_date_parsed",
        "customer_name",
        "city",
        "product_name",
        "category",
        "unit_price_num",
        "quantity",
        "discount",
        "gross_amount",
        "net_amount",
        "payment_method",
        "is_returned"
    ]].rename(columns={
        "order_date_parsed": "order_date",
        "unit_price_num": "unit_price"
    })

    out.to_csv(out_path, index=False)

    # report
    os.makedirs("docs", exist_ok=True)
    with open("docs/data_quality_report.md", "w", encoding="utf-8") as f:
        f.write("# Data Quality Report\n")
        f.write(f"- Rows before cleaning: {before}\n")
        f.write(f"- Rows after cleaning: {after}\n")
        f.write(f"- Dropped rows: {before-after}\n")
        f.write("- Fixes applied: date parsing, city normalization, price cleaning, missing quantity/discount handling\n")

    print(f"? Cleaned data saved: {out_path} ({after} rows)")
    print("? Data quality report: docs/data_quality_report.md")

if __name__ == "__main__":
    main()
