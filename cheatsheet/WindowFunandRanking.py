import pandas as pd
import numpy as np

df = pd.DataFrame({
    'Name': ['John', 'Jane', 'Bob', 'Alice', 'Charlie'],
    'Department': ['IT', 'HR', 'IT', 'Finance', 'Finance'],
    'Salary': [50000, 60000, 75000, 55000, 65000]
})

print("Original DataFrame:")
print(df)

# Cumulative sum by department
print("\nCumulative sum by Department:")
df['Cumsum'] = df.groupby('Department')['Salary'].cumsum()
print(df[['Name', 'Department', 'Salary', 'Cumsum']])

# Rank within group
print("\nRank within Department (by Salary):")
df['Rank'] = df.groupby('Department')['Salary'].rank(ascending=False)
print(df[['Name', 'Department', 'Salary', 'Rank']])

# Percent change
print("\nPercent change (if ordered by salary):")
df_sorted = df.sort_values('Salary')
df_sorted['PctChange'] = df_sorted['Salary'].pct_change() * 100
print(df_sorted[['Name', 'Salary', 'PctChange']])