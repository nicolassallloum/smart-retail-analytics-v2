CREATE INDEX IF NOT EXISTS idx_fact_sales_date ON fact_sales(date_id);
CREATE INDEX IF NOT EXISTS idx_fact_sales_product ON fact_sales(product_id);
CREATE INDEX IF NOT EXISTS idx_fact_sales_customer ON fact_sales(customer_id);
CREATE INDEX IF NOT EXISTS idx_dim_customer_city ON dim_customer(city);

-- Example DBA maintenance commands:
-- VACUUM (ANALYZE);
-- EXPLAIN ANALYZE SELECT ...;
