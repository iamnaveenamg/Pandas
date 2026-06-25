import pandas as pd
import numpy as np

# From Dictionary
data={
    'Name':['Naveen','Praveen','Anand','Tarun'],
    'Age':[25,22,26,25],
    'Salary':[50000,35000,60000,55000]

}

df=pd.DataFrame(data)
print("DataFrame from Dictionary")
print(df)

# From List of Dictionary
data_list=[
    {'Name':'Naveen','Age':25},
    {'Name':'Praveen','Age':22}
]
df2=pd.DataFrame(data_list)
print("\nDataFrame from list of dict")
print(df2)

# From NumPy Array
arr=np.random.randint(0,100,size=(3,3))
df3=pd.DataFrame(arr,columns=['A','B','C'])
print('\nDataFrame from NumPy array')
print(df3)