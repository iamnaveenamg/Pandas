import pandas as pd
import numpy as np

df = pd.DataFrame({
    'Name': ['John', 'Jane', 'Bob'],
    'Age': [25, 28, 30],
    'Salary': [50000, 60000, 75000]
})

# Select Column
print("Column Name:")
print(df['Name'])

# Select Multiple Columns
print("\nColumns,'Name', and 'Age':")
print(df[['Name','Age']])

# Select by Location (iloc)
print("\nFirst row  0 (iloc):")
print(df.iloc[0])

#Select by Label (loc)
print("\n Row with label 0 (loc)")
print(df.loc[0])

#Select by condition
print("\nRows where Age>25:")
print(df[df['Age']>25])
