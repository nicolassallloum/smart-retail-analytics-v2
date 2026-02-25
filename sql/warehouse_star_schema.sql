CREATE TABLE IF NOT EXISTS dim_date (
  date_id SERIAL PRIMARY KEY,
  full_date DATE UNIQUE NOT NULL,
  year INT NOT NULL,
  month INT NOT NULL,
  day INT NOT NULL,
  day_of_week TEXT NOT NULL,
  is_weekend BOOLEAN NOT NULL
);

CREATE TABLE IF NOT EXISTS dim_customer (
  customer_id SERIAL PRIMARY KEY,
  customer_name TEXT NOT NULL,
  city TEXT NOT NULL,
  UNIQUE(customer_name, city)
);

CREATE TABLE IF NOT EXISTS dim_product (
  product_id SERIAL PRIMARY KEY,
  product_name TEXT NOT NULL,
  category TEXT NOT NULL,
  UNIQUE(product_name, category)
);

CREATE TABLE IF NOT EXISTS fact_sales (
  sales_id SERIAL PRIMARY KEY,
  order_ref TEXT NOT NULL,
  date_id INT NOT NULL REFERENCES dim_date(date_id),
  customer_id INT NOT NULL REFERENCES dim_customer(customer_id),
  product_id INT NOT NULL REFERENCES dim_product(product_id),
  quantity NUMERIC(12,2) NOT NULL,
  unit_price NUMERIC(12,2) NOT NULL,
  discount NUMERIC(12,2) NOT NULL,
  gross_amount NUMERIC(12,2) NOT NULL,
  net_amount NUMERIC(12,2) NOT NULL,
  payment_method TEXT NOT NULL,
  is_returned BOOLEAN NOT NULL
);
