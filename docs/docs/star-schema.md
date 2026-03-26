# Star Schema

## Fact Table
### fact_sales
Contains transactional sales metrics and foreign keys to dimensions.

Columns:
- sale_id
- date_id
- customer_id
- product_id
- store_id
- quantity
- unit_price
- total_amount

## Dimension Tables

### dim_customers
- customer_id
- customer_name
- customer_city
- customer_segment

### dim_products
- product_id
- product_name
- category
- brand

### dim_stores
- store_id
- store_name
- region
- province

### dim_dates
- date_id
- full_date
- year
- quarter
- month
- day

## Why Star Schema
A star schema improves query performance, simplifies BI reporting, and supports scalable analytics in enterprise warehouses.
