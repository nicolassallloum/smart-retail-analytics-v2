import os
from datetime import date
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_date, max as _max, countDistinct, sum as _sum, datediff, lit, when

def main(in_path="data/processed/sales_clean.csv", out_dir="data/spark_output"):
    os.makedirs(out_dir, exist_ok=True)

    spark = SparkSession.builder.appName("smart-retail-rfm").getOrCreate()
    df = spark.read.option("header", True).csv(in_path, inferSchema=True)
    df = df.withColumn("order_date", to_date(col("order_date")))

    # reference date = today (or max date + 1 for stability)
    max_date = df.select(_max("order_date").alias("m")).collect()[0]["m"]
    ref_date = max_date

    base = df.filter(col("is_returned") == False)

    rfm = base.groupBy("customer_name", "city").agg(
        _max("order_date").alias("last_purchase_date"),
        countDistinct("order_id").alias("frequency"),
        _sum("net_amount").alias("monetary")
    ).withColumn("recency_days", datediff(lit(ref_date), col("last_purchase_date")))

    # Simple segmentation rules
    seg = rfm.withColumn(
        "segment",
        when((col("frequency") >= 6) & (col("monetary") >= 120) & (col("recency_days") <= 14), "VIP")
        .when((col("recency_days") > 30) & (col("frequency") <= 2), "At-Risk")
        .otherwise("Regular")
    )

    seg.coalesce(1).write.mode("overwrite").option("header", True).csv(f"{out_dir}/customer_segments")
    print("? RFM segments written to:", f"{out_dir}/customer_segments")
    spark.stop()

if __name__ == "__main__":
    main()
