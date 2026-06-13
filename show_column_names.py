import pandas as pd

# List of CSV files to read
csv_files = {
    'purchase_prices.csv': 'data/purchase_prices.csv',
    'purchases.csv': 'data/purchases.csv',
    'sales.csv': 'data/sales.csv',
    'vendor_invoice.csv': 'data/vendor_invoice.csv'
}

# Read each file and display column names
for file_name, file_path in csv_files.items():
    try:
        df = pd.read_csv(file_path)
        print(f"\n{'='*50}")
        print(f"File: {file_name}")
        print(f"{'='*50}")
        print(f"Column Names: {list(df.columns)}")
        print(f"Number of Columns: {len(df.columns)}")
        print(f"Number of Rows: {len(df)}")
    except FileNotFoundError:
        print(f"\nError: {file_path} not found!")
    except Exception as e:
        print(f"\nError reading {file_name}: {str(e)}")
