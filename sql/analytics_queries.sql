-- 1) Total net revenue
SELECT ROUND(SUM(net_amount), 2) AS total_net_revenue
FROM fact_sales
WHERE is_returned = false;

-- 2) Revenue by month
SELECT d.year, d.month, ROUND(SUM(f.net_amount), 2) AS revenue
FROM fact_sales f
JOIN dim_date d ON d.date_id = f.date_id
WHERE f.is_returned = false
GROUP BY d.year, d.month
ORDER BY d.year, d.month;

-- 3) Top 10 products by revenue
SELECT p.product_name, ROUND(SUM(f.net_amount), 2) AS revenue
FROM fact_sales f
JOIN dim_product p ON p.product_id = f.product_id
WHERE f.is_returned = false
GROUP BY p.product_name
ORDER BY revenue DESC
LIMIT 10;

-- 4) Revenue by city
SELECT c.city, ROUND(SUM(f.net_amount), 2) AS revenue
FROM fact_sales f
JOIN dim_customer c ON c.customer_id = f.customer_id
WHERE f.is_returned = false
GROUP BY c.city
ORDER BY revenue DESC;

-- 5) Return rate %
SELECT ROUND(100.0 * AVG(CASE WHEN is_returned THEN 1 ELSE 0 END), 2) AS return_rate_pct
FROM fact_sales;

-- 6) Average order value (AOV)
SELECT ROUND(AVG(order_total), 2) AS avg_order_value
FROM (
  SELECT order_ref, SUM(net_amount) AS order_total
  FROM fact_sales
  WHERE is_returned = false
  GROUP BY order_ref
) t;

-- 7) Payment method distribution
SELECT payment_method, COUNT(*) AS cnt
FROM fact_sales
GROUP BY payment_method
ORDER BY cnt DESC;
