import os
import random
from datetime import datetime, timedelta
from faker import Faker
import pandas as pd

fake = Faker()

CITIES = ["Beirut", "beirut ", " ?????", "Tripoli", "Sidon", "Tyre", "Jounieh", "Zahle", "Byblos"]
PAYMENT_METHODS = ["cash", "card", "wallet"]

PRODUCTS = [
    ("iPhone 14 Case", "Accessories", 12.5),
    ("USB-C Cable", "Accessories", 6.0),
    ("Wireless Mouse", "Electronics", 18.9),
    ("Bluetooth Speaker", "Electronics", 35.0),
    ("Laptop Stand", "Office", 22.0),
    ("Notebook A5", "Office", 3.5),
    ("Protein Bar", "Grocery", 1.8),
    ("Olive Oil 1L", "Grocery", 9.9),
    ("Shampoo 400ml", "Personal Care", 5.2),
    ("Toothpaste", "Personal Care", 2.3),
]

DATE_FORMATS = ["%Y-%m-%d", "%d/%m/%Y", "%b %d %Y"]

def random_date(start: datetime, end: datetime) -> datetime:
    delta = end - start
    return start + timedelta(days=random.randint(0, delta.days))

def maybe_messy_price(price: float) -> str:
    if random.random() < 0.25:
        return f"${price}"
    if random.random() < 0.10:
        return str(price).replace(".", ",")  # 12,5
    return str(price)

def generate(n_rows: int = 10000, out_path: str = "data/raw/sales_raw.csv") -> None:
    os.makedirs(os.path.dirname(out_path), exist_ok=True)

    start = datetime(2025, 10, 1)
    end = datetime(2026, 2, 1)

    rows = []
    for i in range(n_rows):
        order_id = f"ORD-{100000+i}"
        dt = random_date(start, end)

        # mixed date formats
        fmt = random.choice(DATE_FORMATS)
        order_date = dt.strftime(fmt)

        customer_name = fake.name()
        if random.random() < 0.20:
            customer_name = " " + customer_name.lower() + "  "

        city = random.choice(CITIES)

        product_name, category, base_price = random.choice(PRODUCTS)

        unit_price = base_price * random.choice([1, 1, 1, 1.05, 0.95, 1.2])
        unit_price = round(unit_price, 2)
        unit_price_raw = maybe_messy_price(unit_price)

        quantity = random.choice([1, 1, 1, 2, 3, None])  # some missing
        discount = random.choice([0, 0, 0, 1.0, 2.5, None])  # some missing

        payment_method = random.choice(PAYMENT_METHODS)
        returned = random.choice(["N", "N", "N", "Y"])  # 25% returned (synthetic)

        rows.append({
            "order_id": order_id,
            "order_date": order_date,
            "customer_name": customer_name,
            "city": city,
            "product_name": product_name,
            "category": category,
            "unit_price": unit_price_raw,
            "quantity": quantity,
            "discount": discount,
            "payment_method": payment_method,
            "returned": returned
        })

    df = pd.DataFrame(rows)
    df.to_csv(out_path, index=False)
    print(f"? Generated raw data: {out_path} ({len(df)} rows)")

if __name__ == "__main__":
    generate()
