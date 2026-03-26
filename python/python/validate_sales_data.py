import pandas as pd
from pathlib import Path

INPUT_FILE = Path("data/raw/sales_data.csv")

def validate_sales_data(df: pd.DataFrame) -> None:
    required_columns = [
        "sale_id", "sale_date", "customer_id", "customer_name", "customer_city",
        "customer_segment", "product_id", "product_name", "category", "brand",
        "store_id", "store_name", "province", "region", "quantity",
        "unit_price", "total_amount"
    ]

    missing_columns = [col for col in required_columns if col not in df.columns]
    if missing_columns:
        raise ValueError(f"Missing required columns: {missing_columns}")

    if df["sale_id"].duplicated().any():
        raise ValueError("Duplicate sale_id values found")

    if (df["quantity"] <= 0).any():
        raise ValueError("Invalid quantity values found")

    if (df["unit_price"] <= 0).any():
        raise ValueError("Invalid unit_price values found")

    recalculated_total = (df["quantity"] * df["unit_price"]).round(2)
    invalid_totals = df[recalculated_total != df["total_amount"]]
    if not invalid_totals.empty:
        raise ValueError("Some total_amount values do not match quantity * unit_price")

def main():
    df = pd.read_csv(INPUT_FILE)
    validate_sales_data(df)
    print("Sales data validation passed successfully.")

if __name__ == "__main__":
    main()
