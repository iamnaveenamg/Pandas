import pandas as pd
import numpy as np

df=pd.DataFrame({
    'Name': ['John', 'Jane', 'Bob', 'Alice', 'Charlie'],
    'Department': ['IT', 'HR', 'IT', 'Finance', 'Finance'],
    'Salary': [50000, 60000, 75000, 55000, 65000],
    'Bonus': [5000, 3000, 7500, 4000, 6500]
})

print('Original DataFrame')
print(df)

# Group by Single Column
print('\n Total Salary by department')
print(df.groupby('Department')['Salary'].sum())

# Group by with Multiple aggregations
print('\n Salary stats with Department:')
print(df.groupby('Department')['Salary'].agg(['sum','mean', 'count']))

# Group by with multple aggregation on multiple columns
print('\n Multiple Aggregations')
print(df.groupby('Department').agg({'Salary':'sum', 'Bonus':'mean'}))

# Group by with custom function
print('\nTotal Compensation by Department')
print(df.groupby('Department')[['Salary','Bonus']].sum().sum(axis=1))