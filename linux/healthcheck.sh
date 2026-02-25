#!/usr/bin/env bash
set -e

echo "==> Postgres tables:"
docker exec -it sra_postgres psql -U postgres -d smart_retail_dw -c "\dt"

echo "==> Fact row count:"
docker exec -it sra_postgres psql -U postgres -d smart_retail_dw -c "SELECT COUNT(*) AS fact_sales_rows FROM fact_sales;"

echo "✅ Healthcheck done."
