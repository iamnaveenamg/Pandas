import pandas as pd
import numpy as np

df = pd.DataFrame({
    'Name': ['John', 'Jane', 'Bob', 'Alice', 'Charlie'],
    'Age': [25, 28, 30, 26, 35],
    'Salary': [50000, 60000, 75000, 55000, 80000]
})

print("First 2 Rows:")
print(df.head(2))
print("\Last 2 Rows:")
print(df.tail(2))
print('\n Random Sample')
print(df.sample(2))