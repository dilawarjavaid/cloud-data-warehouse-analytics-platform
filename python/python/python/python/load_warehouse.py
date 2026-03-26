from pathlib import Path

CURATED_DIR = Path("data/curated")

def list_files_for_loading():
    files = [
        CURATED_DIR / "dim_customers.csv",
        CURATED_DIR / "dim_products.csv",
        CURATED_DIR / "dim_stores.csv",
        CURATED_DIR / "dim_dates.csv",
        CURATED_DIR / "fact_sales.csv"
    ]
    for file in files:
        print(f"Ready to load into warehouse: {file}")

def simulate_redshift_copy():
    print("Simulating Redshift COPY operations from curated S3 paths...")
    print("COPY dim_customers FROM 's3://bucket/curated/dim_customers.csv' ...")
    print("COPY dim_products FROM 's3://bucket/curated/dim_products.csv' ...")
    print("COPY dim_stores FROM 's3://bucket/curated/dim_stores.csv' ...")
    print("COPY dim_dates FROM 's3://bucket/curated/dim_dates.csv' ...")
    print("COPY fact_sales FROM 's3://bucket/curated/fact_sales.csv' ...")

def main():
    list_files_for_loading()
    simulate_redshift_copy()

if __name__ == "__main__":
    main()
