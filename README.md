# Cloud Data Warehouse Analytics Platform

## Overview
This project demonstrates the design and implementation of a cloud data warehouse pipeline for retail sales analytics.

The solution simulates how raw transactional data is ingested, validated, transformed into a star schema, and loaded into a Redshift-style data warehouse for analytics and BI reporting.

## Business Problem
Retail businesses often receive sales data from multiple stores and channels in raw formats that are not optimized for analytics. This project transforms raw sales data into an analytics-ready warehouse model that supports reporting, KPI tracking, and dashboarding.

## Architecture
The project includes:

1. **Raw Data Generation**
   - Python simulates retail sales data

2. **Validation and Cleansing**
   - Python validates records and handles missing or inconsistent values

3. **Transformation Layer**
   - Python transforms raw data into a dimensional model

4. **Warehouse Layer**
   - Redshift-style fact and dimension tables
   - S3-style raw and curated storage structure

5. **Analytics Layer**
   - SQL queries for revenue, product, region, and customer analysis

6. **Dashboard Layer**
   - Curated outputs for Power BI or Looker dashboards

## Tech Stack
- Python
- Pandas
- SQL
- AWS S3 architecture style
- Amazon Redshift warehouse design
- Star schema modeling
- BI-ready output design

## Data Model
The warehouse uses a star schema with:
- `fact_sales`
- `dim_customers`
- `dim_products`
- `dim_stores`
- `dim_dates`

## Project Structure
```text
docs/    -> Architecture and documentation
data/    -> Raw and curated CSV data
python/  -> Python ETL and transformation scripts
sql/     -> Warehouse DDL and analytics SQL
