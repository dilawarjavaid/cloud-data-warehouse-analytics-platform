import csv
import random
from datetime import datetime, timedelta
from pathlib import Path

RAW_DIR = Path("data/raw")
RAW_DIR.mkdir(parents=True, exist_ok=True)

OUTPUT_FILE = RAW_DIR / "sales_data.csv"

customers = [
    ("C001", "Alice Johnson", "Toronto", "Consumer"),
    ("C002", "Bob Smith", "Mississauga", "Corporate"),
    ("C003", "Charlie Brown", "Ottawa", "Home Office"),
    ("C004", "Diana Lee", "Montreal", "Consumer"),
    ("C005", "Ethan Davis", "Vancouver", "Corporate")
]

products = [
    ("P001", "Laptop", "Electronics", "TechBrand"),
    ("P002", "Phone", "Electronics", "MobilePro"),
    ("P003", "Desk Chair", "Furniture", "ComfortCo"),
    ("P004", "Monitor", "Electronics", "ViewTech"),
    ("P005", "Notebook", "Office Supplies", "PaperPlus")
]

stores = [
    ("S001", "Toronto Downtown", "Ontario", "East"),
    ("S002", "Mississauga Central", "Ontario", "East"),
    ("S003", "Ottawa Market", "Ontario", "East"),
    ("S004", "Montreal Centre", "Quebec", "East"),
    ("S005", "Vancouver Hub", "British Columbia", "West")
]

start_date = datetime(2024, 1, 1)

def generate_sale(sale_num: int) -> list:
    customer = random.choice(customers)
    product = random.choice(products)
    store = random.choice(stores)
    quantity = random.randint(1, 5)
    unit_price = round(random.uniform(20, 2000), 2)
    sale_date = start_date + timedelta(days=random.randint(0, 365))
    total_amount = round(quantity * unit_price, 2)

    return [
        f"SALE{sale_num:05d}",
        sale_date.strftime("%Y-%m-%d"),
        customer[0],
        customer[1],
        customer[2],
        customer[3],
        product[0],
        product[1],
        product[2],
        product[3],
        store[0],
        store[1],
        store[2],
        store[3],
        quantity,
        unit_price,
        total_amount
    ]

def main():
    header = [
        "sale_id",
        "sale_date",
        "customer_id",
        "customer_name",
        "customer_city",
        "customer_segment",
        "product_id",
        "product_name",
        "category",
        "brand",
        "store_id",
        "store_name",
        "province",
        "region",
        "quantity",
        "unit_price",
        "total_amount"
    ]

    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(header)
        for i in range(1, 1001):
            writer.writerow(generate_sale(i))

    print(f"Generated raw sales data at: {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
