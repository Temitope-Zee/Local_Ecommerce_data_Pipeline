import duckdb

con = duckdb.connect('/opt/airflow/transform_project/data/ecommerce.duckdb')

con.execute("""
    CREATE OR REPLACE TABLE raw_orders AS 
    SELECT * FROM read_json_auto('/opt/airflow/transform_project/data/raw/orders.json');
""")
