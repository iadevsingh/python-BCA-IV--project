import pandas as pd

# Read CSV file
df = pd.read_csv("data.csv")

# Display first few rows
print("First 5 rows:")
print(df.head())

# Display basic information
print("\nDataset Info:")
print(df.info())

# Display statistical summary
print("\nStatistical Summary:")
print(df.describe())

# Display column names
print("\nColumns:")
print(df.columns)

# Example: Mean of a column (if numeric column exists)
# Replace 'marks' with your column name
if 'marks' in df.columns:
    print("\nAverage Marks:", df['marks'].mean())