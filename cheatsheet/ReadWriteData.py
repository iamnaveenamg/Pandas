import numpy as np
import pandas as pd

# Read CSV
df=pd.read_csv('foo.csv')
# Write CSV
df.to_csv('output.csv',index=False)
print(df.head())

# Read Excel
df=pd.read_excel('foo.xlsx')
# Write JSON
 #df=pd.read_json('file.json')

df_sample=pd.DataFrame(
    {
        'Date':pd.date_range('2024-01-01',periods=5),
        'product':['A','B','A','C','B'],
        'Sales':[100,150,120,200,180]
    }
)
df_sample.to_csv('sample.csv', index=False)
print('Saved to sample.csv')

# Read it back
df_read=pd.read_csv('sample.csv')
print('\nRead from CSV')
print(df_read)

