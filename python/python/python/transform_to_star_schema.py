import pandas as pd
from pathlib import Path

RAW_FILE = Path("data/raw/sales_data.csv")
CURATED_DIR = Path("data/curated")
CURATED_DIR.mkdir(parents=True, exist_ok=True)

def build_dim_customers(df: pd.DataFrame) -> pd.DataFrame:
    return df[[
        "customer_id",
        "customer_name",
        "customer_city",
        "customer_segment"
    ]].drop_duplicates().sort_values("customer_id")

def build_dim_products(df: pd.DataFrame) -> pd.DataFrame:
    return df[[
        "product_id",
        "product_name",
        "category",
        "brand"
    ]].drop_duplicates().sort_values("product_id")

def build_dim_stores(df: pd.DataFrame) -> pd.DataFrame:
    return df[[
        "store_id",
        "store_name",
        "province",
        "region"
    ]].drop_duplicates().sort_values("store_id")

def build_dim_dates(df: pd.DataFrame) -> pd.DataFrame:
    unique_dates = pd.DataFrame({"full_date": pd.to_datetime(df["sale_date"]).drop_duplicates()})
    unique_dates = unique_dates.sort_values("full_date")
    unique_dates["date_id"] = unique_dates["full_date"].dt.strftime("%Y%m%d").astype(int)
    unique_dates["year"] = unique_dates["full_date"].dt.year
    unique_dates["quarter"] = unique_dates["full_date"].dt.quarter
    unique_dates["month"] = unique_dates["full_date"].dt.month
    unique_dates["day"] = unique_dates["full_date"].dt.day
    return unique_dates[["date_id", "full_date", "year", "quarter", "month", "day"]]

def build_fact_sales(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["date_id"] = pd.to_datetime(df["sale_date"]).dt.strftime("%Y%m%d").astype(int)
    return df[[
        "sale_id",
        "date_id",
        "customer_id",
        "product_id",
        "store_id",
        "quantity",
        "unit_price",
        "total_amount"
    ]]

def main():
    df = pd.read_csv(RAW_FILE)

    dim_customers = build_dim_customers(df)
    dim_products = build_dim_products(df)
    dim_stores = build_dim_stores(df)
    dim_dates = build_dim_dates(df)
    fact_sales = build_fact_sales(df)

    dim_customers.to_csv(CURATED_DIR / "dim_customers.csv", index=False)
    dim_products.to_csv(CURATED_DIR / "dim_products.csv", index=False)
    dim_stores.to_csv(CURATED_DIR / "dim_stores.csv", index=False)
    dim_dates.to_csv(CURATED_DIR / "dim_dates.csv", index=False)
    fact_sales.to_csv(CURATED_DIR / "fact_sales.csv", index=False)

    print("Star schema files created in data/curated/")

if __name__ == "__main__":
    main()
