import os
import json
from pymongo import MongoClient

def main(events_path="data/raw/events.json"):
    mongo_uri = os.getenv("MONGO_URI", "mongodb://localhost:27017")
    db_name = os.getenv("MONGO_DB", "smart_retail")
    col_name = os.getenv("MONGO_COLLECTION", "events")

    client = MongoClient(mongo_uri)
    col = client[db_name][col_name]

    # reload
    col.delete_many({})

    batch = []
    with open(events_path, "r", encoding="utf-8") as f:
        for line in f:
            batch.append(json.loads(line))
            if len(batch) >= 1000:
                col.insert_many(batch)
                batch = []
    if batch:
        col.insert_many(batch)

    print(f"? Loaded MongoDB: {db_name}.{col_name}")
    print("Example queries you can run in Mongo shell:")
    print("db.events.aggregate([{ $group: { _id: '$product_name', views: { $sum: 1 } } }, { $sort: { views: -1 } }])")

if __name__ == "__main__":
    main()
