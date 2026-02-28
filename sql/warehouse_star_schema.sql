-- ===============================
-- DIM DATE
-- ===============================
CREATE TABLE IF NOT EXISTS dim_date (
    date_key INT PRIMARY KEY,
    full_date DATE NOT NULL,
    year INT,
    month INT,
    day INT
);

-- ===============================
-- DIM CUSTOMER
-- ===============================
CREATE TABLE IF NOT EXISTS dim_customer (
    customer_key SERIAL PRIMARY KEY,
    customer_name VARCHAR(255),
    city VARCHAR(100)
);

-- ===============================
-- DIM PRODUCT
-- ===============================
CREATE TABLE IF NOT EXISTS dim_product (
    product_key SERIAL PRIMARY KEY,
    product_name VARCHAR(255),
    category VARCHAR(100),
    unit_price NUMERIC(10,2)
);

-- ===============================
-- FACT SALES
-- ===============================
CREATE TABLE IF NOT EXISTS fact_sales (
    sales_key SERIAL PRIMARY KEY,
    order_id VARCHAR(50),              -- ✅ STRING not INT
    date_key INT REFERENCES dim_date(date_key),
    customer_key INT REFERENCES dim_customer(customer_key),
    product_key INT REFERENCES dim_product(product_key),
    quantity INT,
    discount NUMERIC(10,2),
    gross_amount NUMERIC(12,2),
    net_amount NUMERIC(12,2),
    payment_method VARCHAR(50),
    is_returned BOOLEAN
);