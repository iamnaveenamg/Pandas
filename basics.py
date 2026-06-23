import pandas as pd

# A onde dimensional labeled array capable of holding any data type - Series
s=pd.Series([3,-5,7,4])
index=['a','b','c','d']
print(s)

# A two dimensional labeled data structure with columns of potentially different types - Data Frame
data={
    'Country':['Belgium,','India', 'Brazil'],
    'Capital':['Brussels','New Delhi','Brasolia'],
    'Population':[10000000,10000000,100000]
}

df=pd.DataFrame(data, columns=['Country','Capital','Population'])

print(df)

#print(help(pd.Series.loc))

# A DataFrame is a 2-dimensional data structure that can store data of different types (including characters, integers, floating point values, categorical data and more) in columns
#The index labels each row. By default, this is a sequence of integers starting at 0.

print("Data of Passengers in Titanic")
passengers={
    "Name": [
        "Braund, Mr. Owen Harris",
        "Allen, Mr. William Henry",
        "Bonnell, Miss Elizabeth",
    ],
    "Age": [22, 35, 58],
    "Sex": ["male", "male", "female"],
}
df1=pd.DataFrame(passengers)
print(df1['Age'])

print('\n Creating Ages Series')
Ages=pd.Series([22,35,58],name='Age')

print(df1['Age'].max())
print(Ages.max())
print(df1.describe())
