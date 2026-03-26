import pandas as pd
from pathlib import Path

CURATED_DIR = Path("data/curated")
OUTPUT_FILE = CURATED_DIR / "dashboard_sales_summary.csv"

def main():
    fact_sales = pd.read_csv(CURATED_DIR / "fact_sales.csv")
    dim_stores = pd.read_csv(CURATED_DIR / "dim_stores.csv")
    dim_products = pd.read_csv(CURATED_DIR / "dim_products.csv")

    merged = fact_sales.merge(dim_stores, on="store_id", how="left")
    merged = merged.merge(dim_products, on="product_id", how="left")

    dashboard_summary = merged.groupby(["region", "province", "category"], as_index=False).agg(
        total_revenue=("total_amount", "sum"),
        total_quantity=("quantity", "sum"),
        total_transactions=("sale_id", "count")
    )

    dashboard_summary.to_csv(OUTPUT_FILE, index=False)
    print(f"Dashboard summary exported to: {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
