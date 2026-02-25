#!/usr/bin/env bash
set -e

echo "============================================"
echo " SMART RETAIL ANALYTICS PIPELINE STARTING "
echo "============================================"

# -------------------------------------------
# 1) Generate Raw Data
# -------------------------------------------
echo "==> 1) Generate raw sales CSV"
python3 etl/generate_raw_data.py

# -------------------------------------------
# 2) Clean & Transform
# -------------------------------------------
echo "==> 2) Clean & transform"
python3 etl/clean_transform.py

# -------------------------------------------
# 3) Create Warehouse Schema (Inside Container)
# -------------------------------------------
echo "==> 3) Create warehouse schema (inside container)"
docker exec -i sra_postgres psql -U postgres -d smart_retail_dw < sql/warehouse_star_schema.sql
docker exec -i sra_postgres psql -U postgres -d smart_retail_dw < sql/indexes_and_dba.sql

# -------------------------------------------
# 4) Load into PostgreSQL (Inside Docker Network)
# -------------------------------------------
echo "==> 4) Load into PostgreSQL (inside Docker network)"

docker run --rm \
  --network smart-retail-analytics_default \
  -v $(pwd):/app \
  -w /app \
  python:3.12 \
  bash -c "
    pip install pandas sqlalchemy psycopg2-binary python-dateutil numpy >/dev/null 2>&1 &&
    python etl/load_to_postgres.py
  "

# -------------------------------------------
# 5) Verify Fact Row Count
# -------------------------------------------
echo "==> 5) Verifying fact table row count"
docker exec -i sra_postgres psql -U postgres -d smart_retail_dw -c "SELECT COUNT(*) AS fact_sales_rows FROM fact_sales;"

# -------------------------------------------
# 6) Run Spark KPIs
# -------------------------------------------
echo "==> 6) Running Spark KPI job"
python3 spark/spark_kpis.py

echo "==> 7) Running Spark RFM segmentation"
python3 spark/spark_rfm_segmentation.py

# -------------------------------------------
# 8) Generate & Load NoSQL Events
# -------------------------------------------
echo "==> 8) Generate NoSQL events"
python3 nosql/generate_events.py

echo "==> 9) Load events into MongoDB"
python3 nosql/load_events.py

# -------------------------------------------
# Pipeline Completed
# -------------------------------------------
echo "============================================"
echo " PIPELINE COMPLETED SUCCESSFULLY "
echo "============================================"
