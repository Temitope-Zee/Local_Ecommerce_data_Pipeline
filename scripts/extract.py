import json
import os

orders_data = [
    {"order_id": 101, "customer_id": 1, "product": "Laptop", "price": 1200.00, "date": "2026-10-01"},
    {"order_id": 102, "customer_id": 2, "product": "Mouse", "price": 25.50, "date": "2026-10-02"},
    {"order_id": 103, "customer_id": 1, "product": "Keyboard", "price": 75.00, "date": "2026-10-03"}
]

os.makedirs("/opt/airflow/transform_project/data/raw", exist_ok=True)
file_path = "/opt/airflow/transform_project/data/raw/orders.json"

with open(file_path, "w") as f:
    json.dump(orders_data, f, indent=4)

print(f"Successfully extracted data to {file_path}")
