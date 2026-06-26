import pandas as pd
import numpy as np


df = pd.DataFrame({
    'Age': [25, 28, 30, 26, 29],
    'Salary': [50000, 60000, 75000, 55000, 65000],
    'Bonus': [5000, 6000, 7500, 5500, 6500]
})

print("Original DataFrame:")
print(df)

# Descriptive Statistics
print('\nDescribe:')
print(df.describe())

# Specific Stats
print(f"\nMean Age: {df['Age'].mean()}")
print(f"Median Salary: {df['Salary'].median()}")
print(f"Std Dev Bonus: {df['Bonus'].std()}")
print(f"Variance Age: {df['Age'].var()}")

# Correlation
print("\nCorrelation matrix:")
print(df.corr())

# Quantiles
print("\n75th percentile of Salary:")
print(df['Salary'].quantile(0.75))