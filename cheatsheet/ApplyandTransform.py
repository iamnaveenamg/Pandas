import pandas as pd
import numpy as np


df = pd.DataFrame({
    'Age': [25, 28, 30],
    'Salary': [50000, 60000, 75000]
})

print("Original DataFrame:")
print(df)

# Apply function to column
print('\nApply customer function (square)')
df['Age_squared']=df['Age'].apply(lambda x:x**2)
print(df[['Age','Age_squared']])

#Apply to multiple columns
print('\n Apply Custom functions to multiple columns')
df['Both_squared']=df[['Age','Salary']].apply(lambda row:row['Age']**2 + row['Salary']**2, axis=1)
print(df[['Age', 'Salary', 'Both_squared']])

# Transform (Standardization)
#from sklearn.preprocessing import StandardScalar
print('\n Transform Standardization:')
df_copy=df.copy()
df_copy['Salary_standardized']=(df_copy['Salary']-df_copy['Salary'].mean()) / df_copy['Salary'].std()
print(df_copy[['Salary','Salary_standardized']])