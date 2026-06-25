# Data Cleaning - Missing Values
import pandas as pd
import numpy as np

# Create data with missing values
df = pd.DataFrame({
    'Name': ['John', 'Jane', 'Bob', 'Alice'],
    'Age': [25, np.nan, 30, np.nan],
    'Salary': [50000, 60000, np.nan, 55000]
})

print("DataFrame with missing values:")
print(df)

# Check for missing values
print("\nMissing values:")
print(df.isnull())

print("\nCount of missing values:")
print(df.isnull().sum())

# Drop rows with any missing value
print("\nAfter dropna():")
print(df.dropna())

# Fill missing values
print("\nAfter fillna(0):")
print(df.fillna(0))

# Fill with specific values per column
print("\nAfter fillna with mean:")
df_filled = df.copy()
df_filled['Age'] = df_filled['Age'].fillna(df_filled['Age'].mean())
print(df_filled)