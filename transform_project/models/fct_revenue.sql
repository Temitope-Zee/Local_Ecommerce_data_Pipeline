{{ config(materialized='table') }}

SELECT
    product,
    COUNT(order_id) AS total_orders,
    SUM(price) AS total_revenue,
    AVG(price) AS avg_order_price,
    MAX(date) as last_order_date
FROM {{ source('ecommerce', 'raw_orders') }}
GROUP BY product
