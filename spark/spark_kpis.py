import os
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_date, sum as _sum, count as _count, desc

def main(in_path="data/processed/sales_clean.csv", out_dir="data/spark_output"):
    os.makedirs(out_dir, exist_ok=True)

    spark = SparkSession.builder.appName("smart-retail-kpis").getOrCreate()
    df = spark.read.option("header", True).csv(in_path, inferSchema=True)

    df = df.withColumn("order_date", to_date(col("order_date")))
    df_valid = df.filter(col("is_returned") == False)

    revenue_by_day = df_valid.groupBy("order_date").agg(_sum("net_amount").alias("revenue")).orderBy("order_date")
    top_products = df_valid.groupBy("product_name").agg(_sum("net_amount").alias("revenue")).orderBy(desc("revenue")).limit(10)
    revenue_by_city = df_valid.groupBy("city").agg(_sum("net_amount").alias("revenue")).orderBy(desc("revenue"))

    revenue_by_day.coalesce(1).write.mode("overwrite").option("header", True).csv(f"{out_dir}/kpi_revenue_by_day")
    top_products.coalesce(1).write.mode("overwrite").option("header", True).csv(f"{out_dir}/kpi_top_products")
    revenue_by_city.coalesce(1).write.mode("overwrite").option("header", True).csv(f"{out_dir}/kpi_revenue_by_city")

    print("? Spark KPI outputs written to:", out_dir)
    spark.stop()

if __name__ == "__main__":
    main()
