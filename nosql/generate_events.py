import os
import json
import random
from datetime import datetime, timedelta
from faker import Faker

fake = Faker()

EVENTS = ["product_view", "add_to_cart", "checkout", "session_start"]
DEVICES = ["android", "ios", "web"]
CITIES = ["Beirut", "Tripoli", "Sidon", "Tyre", "Jounieh", "Zahle"]

PRODUCTS = ["USB-C Cable", "Wireless Mouse", "Olive Oil 1L", "Shampoo 400ml", "Laptop Stand"]

def main(n=5000, out_path="data/raw/events.json"):
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    now = datetime.utcnow()

    docs = []
    for _ in range(n):
        ts = now - timedelta(minutes=random.randint(0, 60*24*30))
        docs.append({
            "event_id": fake.uuid4(),
            "ts": ts.isoformat(),
            "event_type": random.choice(EVENTS),
            "customer_name": fake.name(),
            "city": random.choice(CITIES),
            "device": random.choice(DEVICES),
            "product_name": random.choice(PRODUCTS),
            "session_id": fake.uuid4()
        })

    with open(out_path, "w", encoding="utf-8") as f:
        for d in docs:
            f.write(json.dumps(d) + "\n")

    print(f"? Events generated: {out_path} ({n} lines)")

if __name__ == "__main__":
    main()
