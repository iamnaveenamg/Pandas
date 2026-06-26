import pandas as pd
import numpy as np

# Pivot Table- Total Sales by product and Region
# Region - East, West, North ,South

df = pd.DataFrame({
    'Product': ['A', 'B', 'A', 'B', 'A', 'B'],
    'Region': ['East', 'East', 'West', 'West', 'North', 'North'],
    'Sales': [300, 400, 400, 350, 250, 350],
    'Date': pd.date_range('2024-01-01', periods=6)
})

print("Original DataFrame:")
print(df)

# Simple pivot Table
print('\nPivot: Sales by Product and Region')
pivot=df.pivot_table(values='Sales', index='Product', columns='Region', aggfunc='sum')
print(pivot)

# Pivot with Multiple Aggregations
print('\nPivot: Mean and Sum:')
pivot2=df.pivot_table(values='Sales', index='Product',columns='Region',aggfunc=['sum','mean'])
print(pivot2)

# Unstack
print('\nUsing unstack (simmilar to pivot)')
grouped=df.groupby(['Product','Region'])['Sales'].sum()
print(grouped)
print(grouped.unstack())