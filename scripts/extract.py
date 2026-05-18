import pandas as pd

# Path to dataset
file_path = r"data/raw/Sample - Superstore.csv"

# Read CSV
df = pd.read_csv(file_path, encoding='latin1')

# Display first 5 rows
print("\nFIRST 5 ROWS:")
print(df.head())

# Display column names
print("\nCOLUMN NAMES:")
print(df.columns)

# Dataset info
print("\nDATASET INFO:")
print(df.info())

# Check missing values
print("\nMISSING VALUES:")
print(df.isnull().sum())