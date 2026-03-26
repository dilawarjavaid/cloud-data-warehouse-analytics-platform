COPY retail_analytics.dim_customers
FROM 's3://your-bucket/curated/dim_customers.csv'
IAM_ROLE 'arn:aws:iam::123456789012:role/RedshiftRole'
CSV
IGNOREHEADER 1;

COPY retail_analytics.dim_products
FROM 's3://your-bucket/curated/dim_products.csv'
IAM_ROLE 'arn:aws:iam::123456789012:role/RedshiftRole'
CSV
IGNOREHEADER 1;

COPY retail_analytics.dim_stores
FROM 's3://your-bucket/curated/dim_stores.csv'
IAM_ROLE 'arn:aws:iam::123456789012:role/RedshiftRole'
CSV
IGNOREHEADER 1;

COPY retail_analytics.dim_dates
FROM 's3://your-bucket/curated/dim_dates.csv'
IAM_ROLE 'arn:aws:iam::123456789012:role/RedshiftRole'
CSV
IGNOREHEADER 1;

COPY retail_analytics.fact_sales
FROM 's3://your-bucket/curated/fact_sales.csv'
IAM_ROLE 'arn:aws:iam::123456789012:role/RedshiftRole'
CSV
IGNOREHEADER 1;
