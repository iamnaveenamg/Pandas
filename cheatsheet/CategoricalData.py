import pandas as pd
import numpy as np

df = pd.DataFrame({
    'Product': ['A', 'B', 'A', 'C', 'B', 'A'],
    'Priority': ['High', 'Low', 'Medium', 'High', 'Low', 'Medium']
})

print("Original dtypes:")
print(df.dtypes)

# Convert to categorical
df['Product'] = pd.Categorical(df['Product'])
df['Priority'] = pd.Categorical(
    df['Priority'],
    categories=['Low', 'Medium', 'High'],
    ordered=True
)

print("\nAfter converting to categorical:")
print(df.dtypes)

print("\nValue counts for Priority:")
print(df['Priority'].value_counts().sort_index())

print("\nOrdered categorical (Low < Medium < High):")
print(df[df['Priority'] > 'Low'])