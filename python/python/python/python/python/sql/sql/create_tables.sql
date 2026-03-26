CREATE TABLE retail_analytics.dim_customers (
    customer_id VARCHAR(20) PRIMARY KEY,
    customer_name VARCHAR(100),
    customer_city VARCHAR(100),
    customer_segment VARCHAR(50)
);

CREATE TABLE retail_analytics.dim_products (
    product_id VARCHAR(20) PRIMARY KEY,
    product_name VARCHAR(100),
    category VARCHAR(100),
    brand VARCHAR(100)
);

CREATE TABLE retail_analytics.dim_stores (
    store_id VARCHAR(20) PRIMARY KEY,
    store_name VARCHAR(100),
    province VARCHAR(100),
    region VARCHAR(50)
);

CREATE TABLE retail_analytics.dim_dates (
    date_id INTEGER PRIMARY KEY,
    full_date DATE,
    year INTEGER,
    quarter INTEGER,
    month INTEGER,
    day INTEGER
);

CREATE TABLE retail_analytics.fact_sales (
    sale_id VARCHAR(20) PRIMARY KEY,
    date_id INTEGER,
    customer_id VARCHAR(20),
    product_id VARCHAR(20),
    store_id VARCHAR(20),
    quantity INTEGER,
    unit_price DECIMAL(10,2),
    total_amount DECIMAL(12,2)
);
