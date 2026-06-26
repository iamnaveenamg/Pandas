import pandas as pd
import numpy as np

# Create two DataFrames
df1 = pd.DataFrame({
    'ID': [1, 2, 3],
    'Name': ['John', 'Jane', 'Bob'],
    'Salary': [50000, 60000, 75000]
})

df2 = pd.DataFrame({
    'ID': [1, 2, 3],
    'Department': ['IT', 'HR', 'IT']
})

print("DataFrame 1:")
print(df1)
print("\nDataFrame 2:")
print(df2)


#Inner Join
print('\n Inner Join')
merged=pd.merge(df1,df2, on='ID')
print(merged)

# Left merge
df3=pd.DataFrame({'ID':[1, 2, 4], 'Location':['NYC','LA','Chicago']})
print('\n Left merge includes all from df1')
print(pd.merge(df1,df3,on='ID',how='left'))

# Concatenate
df4 = pd.DataFrame({
    'ID': [4, 5],
    'Name': ['Alice', 'Charlie'],
    'Salary': [55000, 65000]
})
print('\nConcatenate Vertically')
print(pd.concat([df1,df4],ignore_index=True))
