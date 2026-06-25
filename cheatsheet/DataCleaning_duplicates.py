import numpy as np
import pandas as pd

# Create data with duplicates
df = pd.DataFrame({
    'Name': ['John', 'Jane', 'John', 'Bob', 'Jane'],
    'Age': [25, 28, 25, 30, 28],
    'City': ['NYC', 'LA', 'NYC', 'Chicago', 'LA']
})

print("Original DataFrame with duplicates:")
print(df)

# Check for duplicates
print("\nDuplicate rows:")
print(df.duplicated())

# Drop duplicates
print("\nAfter drop_duplicates():")
print(df.drop_duplicates())

# Drop duplicates based on specific columns
print("\nAfter drop_duplicates(subset=['Name']):")
print(df.drop_duplicates(subset=['Name']))

# Keep last occurrence
print("\nKeep last duplicate:")
print(df.drop_duplicates(keep='last'))
     