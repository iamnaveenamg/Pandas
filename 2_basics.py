import numpy as np
import pandas as pd

# Series: 1D Labeled array holding data of any type
# DataFrame: 2D Data structure that holds data like a 2D array or a table with rows and columns

# Object Creation
s=pd.Series([1,3,5,np.nan,6,8])
#print(s)

# Creating a DataFrame by passing a NumPy array with a datetime index using data_range() and labeled columns
dates=pd.date_range("20130101",periods=10)
#print(dates)

df=pd.DataFrame(np.random.randn(10,4), index=dates, columns=list("ABCD"))

#print(df)

# Creating a DataFrame by passing a dictionary of objects where the keys are column labels and the values are column values
df2=pd.DataFrame(
    {
        "A": 1.0,
        "B": pd.Timestamp("20130102"),
        "C": pd.Series(1,index=list(range(4)),dtype="float32"),
        "D": np.array([3]*4, dtype="int32"),
        "E": pd.Categorical(["test","train","test","train"]),
        "F":"Foo"
    }
)

#print(df2.dtypes)

# Viewing Data
# 1. DataFrame.head() and DataFrame.tail() to view the top and bottom rows of the frame respectively
print(df.head()) ,print(df.tail(3))
# 2. Display the DataFrame.index or DataFrame.columns
print(df.columns)

# 3.  Return a NumPy representation of the underlying data with DataFrame.to_numpy() without the index or column labels
print(df2.to_numpy())

print(df.describe())

# Transposing your Data
print(df.T)

# DataFrame.sort_index() sort by an axis

print(df.sort_index(axis=1, ascending=True))

# DataFrame.sort_values() sorts by values
print(df.sort_values(by='B'))

## Getitem []
#1. For a DataFrame, passing a single label selects a column and yields a series
print(df["A"])

#2. If the label only contains letters, numbers and underscores, you can alternatively use the column name attributes
print("The Values of A")
print(df.A)

#3.Passing a list of column labes selects multiple columns, which can be usefull for getting a subset or rearranging
print(df[["B","A"]])

#4. For a DataFrame, passing : selects matching rows
print(df[0:3])
print(df['20130102':'20130104'])

# Selection by Label
#1. Selecting a row matching a label
print(df.loc[dates[0]])
#2. Selecting all rows (:) with a select column labels
print(df.loc[:,["A", "B"]])

#3. For label slicing, bot endpoints are included
print(df.loc["20130102":"20130104", ["A", "B"]])

#4. Selecting a single row and Column  label returns scalar
print(df.loc[dates[0], "A"])

#5. For getting fast access to a scalar()
print(df.at[dates[0], "A"])

## Selection by Position
#1. Select via the position of the passed integers
print(df.iloc[3])

#2. Integer slices acts similar to NumPy or Python
print(df.iloc[3:5,0:2])

#3. Lits of integer position locations
print(df.iloc[[1,2,4],[0,2]])

#4. For slicing rows explicitly
print(df.iloc[1:3,:])

#5. For slicing columns explicitly
print(df.iloc[:, 1:3])

#6. For getting a value explicitly
print(df.iloc[1,1])
#7. For getting fast access to a scalar (Equivalent to the prioor methods)
print(df.iat[1,1])

## Boolean Indexing
print(df[df["A"]>0]) # 1. Select rows where df.A is greater than 0
print(df[df>0]) # 2. Selecting values from a Dataframe where a boolean condition is met
 # 3. Using isin() method for filtering
print(df)
df2=df.copy()
df2["E"]=["One","one","two","Three","Four","Three","Five","Six","Seven","Nine"]
print(df2)
print(df2[df2["E"].isin(["two","Four"])])

#Setting
print("New Settings")

# Setting a new column automatically aligns the data by the indexes
s1=pd.Series(
    [1,2,3,4,5,6,7,8,9,10],
    index=pd.date_range("20130102", periods=10)
)
print(s1)
df["F"]=s1
 # Setting values by label:
df.at[dates[0],"A"]=0
 # Setting Values by position
df.iat[0,1]=0

# Setting by assigning with a NumPy array:
df.loc[:,"D"]=np.array([5]*len(df))
print(df)
# A where operation with setting
df2=df.copy()
df2[df2>0]=-df2
print(df2)


## Missing Data
# For NumPy data types, np.nan represents missing data. It is by defauly not included in computations.
# Reindexing allows to change/add/delete the index on a specified axis. This returns a copy of the data

df1=df.reindex(index=dates[0:4], columns=list(df.columns)+["E"])
df1.loc[dates[0]:dates[1],"E"]=1
print(df1)

print(df1.dropna(how="any"))# DataFrame.dropna() drops any that have missing data:
print(df1.fillna(value=5)) # DataFrame.fillna() fills missing data:
print(pd.isna(df1)) #isna() gets the boolean mask where values are nan


### Operations
# Stats: Operations in general exclude missing data
print(df.mean()) # Calculate the mean value for each column
print(df.mean(axis=1)) # calculate the mean value for each row
# Operating with another Series or DataFrame with a different index or column will align the result with the union of the index or column labels. In addition, pandas automatically broadcasts along the specified dimension and will fill unaligned labels with np.nan.
s=pd.Series([1,3,5,np.nan, 6, 8,9,10,2, 4], index=dates).shift(2)
print(s)
print(df.sub(s, axis="index"))


## User Defined Functions
# DataFrame.agg() and DataFrame.transform() applies a user defined function that reduces or broadcasts its result
print(df.agg(lambda x:np.mean(x)*5.6))

print(df.transform(lambda x:x*101.2))

# Value Counts
s=pd.Series(np.random.randint(0,7, 10))
print(s)
print(s.value_counts())

## String Methods
 #1. Series is equipped with a set o string processing methods in the str attribute that make it easy to operate on each element of the array, as in the code.
s=pd.Series(["A","B","C","Aaba","Baca",np.nan,"CABA","dog","cat"])
print(s.str.lower())

### Merge
# 1.Concat
df=pd.DataFrame(np.random.randn(10,4))
print(df)
pieces=[df[:3],df[3:7],df[7:]]
print(pieces)

print(pd.concat(pieces))

# 2. merge() enables SQL style join types along specific columns
left=pd.DataFrame({"Key":["foo","fpp"], "lval":[1,2]})
right=pd.DataFrame({"Key":["foo", "foo"], "rval":[4,5]})
print(left)
print(right)
print(pd.merge(left,right, on="Key"))

# 3. Grouping - By "group  by"  we are referring to a process involving one or more of the following steps:
 # a. Splitting the data into groups based on some criteria
 # b. Applying a function to each group independently
 # c. Combining the results into a data structure

print("The Grouping in Pandas")
df=pd.DataFrame(
    {
        "A":["foo","bar","foo","bar","foo","bar","foo","foo"],
        "B":["one","one","two","three","two","two","one","three"],
        "C":np.random.randn(8),
        "D":np.random.randn(8),
    }
)
print(df)

# Grouping by a column label, selecting column labels, and then applying the DataFrameGroupBy.sum()
print("Find the Group by Value using")
print(df.groupby("A")[["C","D"]].sum())
print(df.groupby(["A","B"]).sum()) # Grouping by multiple columns label forms MultiIndex

# Reshaping

# 1. Stack
print("The Stack value of Reshaping")
arrays=[
    ["bar","bar","baz","baz","foo","foo", "qux","qux"],
    ["one","two","one","two","one","two","one","two"]
]
index=pd.MultiIndex.from_arrays(arrays,names=["first","second"])  
df=pd.DataFrame(np.random.randn(8,2),index=index, columns=["A","B"])
df2=df[:4]
print(df2)
 # The stack() method "compresses" a level in the DataFrame's columns
stacked=df2.stack()
print(stacked)
# With a stacked DataFrame or Series, the inverse operation of stack() is unstack(), which by default unstacks the last level
print(stacked.unstack())
print(stacked.unstack(1))
print(stacked.unstack(0))


# Pivot Tables
print("Operation on Pivot Table")
df=pd.DataFrame(
    {
        "A":["one","one","two","three"]*3,
        "B":["A","B","C"]*4,
        "C":["foo","foo","foo","bar","bar","bar"]*2,
        "D":np.random.randn(12),
        "E":np.random.randn(12)

    }
)
print(df)
 # pivot_table() pivots a DataFrame specifying the Values, Index and Columns
 # Pivot Table is powerful spreadsheet and database tool used to summasize, group and analyze large amounts of raw data.
print(pd.pivot_table(df, values="D",index=["A","B"],columns=["C"]))


## Time Series - pandas has simple, powerful, and efficient functionality for performing resampling operations during frequency conversion (e.g., converting secondly data into 5-minutely data).
rng=pd.date_range("1/1/2012", periods=100, freq="s")
ts=pd.Series(np.random.randint(0,500,len(rng)), index=rng)
print(ts.resample("5Min").sum())

 # Series.tz_localize() localizes a time series to time zone
rng=pd.date_range("3/6/2012 00:00",periods=5, freq="D")
ts=pd.Series(np.random.randn(len(rng)),rng)
print(ts)
ts_utc=ts.tz_localize("UTC")
print(ts_utc)
 # Series.tz_convert() converts a timezones aware time series rto another time zone
print(ts_utc.tz_convert("US/Eastern"))
 # Adding a non fized duration to a time series
print(rng)
print(rng+pd.offsets.BusinessDay(5))

# Categoricals

df=pd.DataFrame(
    {"id":[1,2,3,4,5,6],"raw_grade":["a","b","b","a","a","e"]}
)
 # Converting the raw grades to a categorical data type
df["grade"]=df["raw_grade"].astype("category")
print(df["grade"])
 # Rename the categories to more meaningful names
new_categories=["very good","good", "very bad"]
df["grade"]=df["grade"].cat.rename_categories(new_categories)
 # Reorder the categories and simultaneously add the missing categories
df["grade"]=df["grade"].cat.set_categories(
    ["very bad","bad","medium","good","very good"]
)
print(df["grade"])
 # Sorting is per order in the categories, not lexical order
print(df.sort_values(by="grade"))
 # Grouping by a categorical column with observed=False also shwos empty categories
print(df.groupby("grade",observed=False).size())

# Plotting

import matplotlib as plt

#print(plt.close("all"))
ts=pd.Series(np.random.randn(1000),index=pd.date_range("1/1/2000",periods=1000))
ts=ts.cumsum()
ts.plot()

# Plots all columns
df = pd.DataFrame(
    np.random.randn(1000, 4), index=ts.index, columns=["A", "B", "C", "D"]
)
 
df = df.cumsum()
#plt.figure();
df.plot();
#plt.legend(loc='best');

## Importing and Exporting Data
# CSV

df=pd.DataFrame(np.random.randint(0,5,(10,5)))
df.to_csv("foo.csv")
print(pd.read_csv("foo.csv"))

# Parquet
df.to_parquet("foo.parquet")
print(pd.read_parquet("foo.parquet"))

#Excel
df.to_excel("foo.xlsx",sheet_name="Sheet1")
print(pd.read_excel("foo.xlsx","Sheet1",index_col=None, na_values=["NA"]))


# Gotchas
# attempting to perform a boolean operation on a Series or DataFrame you might see an exception like:

if pd.Series([False, True, False]):
    print("Y was true")
    
