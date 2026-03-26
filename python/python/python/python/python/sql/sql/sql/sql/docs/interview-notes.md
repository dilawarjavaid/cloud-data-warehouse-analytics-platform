# Interview Talking Points

## What this project demonstrates
- End-to-end cloud data warehouse design
- Python ETL development
- Data validation and cleansing
- Star schema modeling
- SQL analytics for reporting
- Dashboard-ready output design

## Why I built it
I wanted to demonstrate how raw transactional data can be transformed into an enterprise-ready dimensional warehouse model for scalable analytics and BI use cases.

## Key design decisions
- Used Python for ingestion, validation, and transformation
- Used a star schema to simplify reporting and optimize warehouse queries
- Separated raw and curated layers to reflect cloud data lake and warehouse patterns
- Structured outputs for downstream dashboard tools like Power BI or Looker

## AWS mapping
- Raw and curated data stored in S3-style zones
- Warehouse modeled for Redshift loading using COPY commands

## GCP mapping
- The same design could be implemented using Cloud Storage and BigQuery with minimal architecture changes
