import pandas as pd
import numpy as np

df=pd.DataFrame({
    'Name':['Naveen','Praveen','Anand'],
    'Age':[25,22,26],
    'Salary':[50000,60000,70000]
})

print(f'Shape: {df.shape}')
print(f'\n Columns: {df.columns.tolist()}')
print(f'\n Index: {df.index.tolist()}')
print(f'Data Types: \n {df.dtypes}')
print(f'\nMemory Usage:\n{df.memory_usage()}')
print(f'\nInfo:\n {df.info()}')
