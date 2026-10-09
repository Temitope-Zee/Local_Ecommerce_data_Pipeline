SELECT 
    order_id,
    customer_id,
    product,
    price,
    date::DATE as order_date
FROM {{ source('transform_project', 'raw_orders') }}
