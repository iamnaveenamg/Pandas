import pandas as pd
import numpy as np

df = pd.DataFrame({
    'Name': ['John', 'Jane', 'Bob', 'Alice'],
    'Age': [25, 28, 30, 26],
    'Salary': [50000, 60000, 75000, 55000],
    'Department': ['IT', 'HR', 'IT', 'Finance']
})

# Single condition filter
print("Age > 26:")
print(df[df['Age'] > 26])

# Multiple conditions (AND)
print("\nAge > 25 AND Salary > 55000:")
print(df[(df['Age'] > 25) & (df['Salary'] > 55000)])

# Multiple conditions (OR)
print("\nDepartment = IT OR Age > 28:")
print(df[(df['Department'] == 'IT') | (df['Age'] > 28)])

# Sort by single column
print("\nSorted by Salary (ascending):")
print(df.sort_values('Salary'))

# Sort by multiple columns
print("\nSorted by Department then Salary (descending):")
print(df.sort_values(['Department', 'Salary'], ascending=[True, False]))

# Using isin()
print("\nDepartment in ['IT', 'Finance']:")
print(df[df['Department'].isin(['IT', 'Finance'])])