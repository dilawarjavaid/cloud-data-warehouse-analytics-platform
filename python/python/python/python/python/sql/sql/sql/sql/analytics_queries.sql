SELECT
    ds.region,
    dp.category,
    SUM(fs.total_amount) AS total_revenue,
    SUM(fs.quantity) AS total_units_sold,
    COUNT(fs.sale_id) AS total_transactions
FROM retail_analytics.fact_sales fs
JOIN retail_analytics.dim_stores ds
    ON fs.store_id = ds.store_id
JOIN retail_analytics.dim_products dp
    ON fs.product_id = dp.product_id
GROUP BY ds.region, dp.category
ORDER BY total_revenue DESC;

SELECT
    dc.customer_segment,
    SUM(fs.total_amount) AS revenue_by_segment
FROM retail_analytics.fact_sales fs
JOIN retail_analytics.dim_customers dc
    ON fs.customer_id = dc.customer_id
GROUP BY dc.customer_segment
ORDER BY revenue_by_segment DESC;

SELECT
    dd.year,
    dd.month,
    SUM(fs.total_amount) AS monthly_revenue
FROM retail_analytics.fact_sales fs
JOIN retail_analytics.dim_dates dd
    ON fs.date_id = dd.date_id
GROUP BY dd.year, dd.month
ORDER BY dd.year, dd.month;
