# Architecture

## High-Level Design

### 1. Raw Data Layer
Sales transactions are generated as raw CSV files and stored in a raw zone similar to cloud object storage.

### 2. Validation Layer
Python scripts validate schema, data types, and business rules before transformation.

### 3. Transformation Layer
Raw data is converted into warehouse-ready dimension and fact tables using dimensional modeling.

### 4. Curated Layer
Transformed datasets are written into curated outputs, simulating S3 curated storage.

### 5. Warehouse Layer
Fact and dimension tables are modeled for Redshift-style loading and analytics.

### 6. Analytics Layer
SQL queries calculate KPIs, revenue metrics, product performance, and customer insights.

### 7. Dashboard Layer
Curated query outputs can feed Power BI or Looker dashboards.

## Cloud Mapping
AWS:
- S3 for raw and curated storage
- Redshift for analytics warehouse

GCP Equivalent:
- Cloud Storage for raw and curated storage
- BigQuery for analytics warehouse
