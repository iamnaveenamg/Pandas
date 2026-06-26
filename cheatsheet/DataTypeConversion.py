import pandas as pd
import numpy as np

df=pd.DataFrame({
    'Name':['John','Jane','Bob'],
    'Age':['25','28','30'],
    'Salary':['30000','40000','50000']
})

print("Original Data Types")
print(df.dtypes)

# convert to numeric
df['Age']=df['Age'].astype(int)
df['Salary']=df['Salary'].astype(float)

print('\nAfter Conversion')
print(df.dtypes)
print('\nDataFrame')
print(df)

# Convert to datetime
df2=pd.DataFrame({'Date':['2024-01-01','2024-01-02']})
df2['Date']=pd.to_datetime(df2['Date'])
print('\n Converted to Datetime')
print(df2.dtypes)