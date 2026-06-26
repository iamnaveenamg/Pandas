import pandas as pd
import numpy as np


df = pd.DataFrame({
    'Name': ['john', 'jane', 'bob'],
    'Email': ['john@example.com', 'jane@example.com', 'bob@example.com']
})

print("Original:")
print(df)

# String methods
print("\nUppercase:")
print(df['Name'].str.upper())

print("\nLength:")
print(df['Name'].str.len())

print("\nCapitalize:")
print(df['Name'].str.capitalize())

print("\nContains 'a':")
print(df['Name'].str.contains('a'))

print("\nExtract domain (after @):")
print(df['Email'].str.extract(r'@(\w+)'))