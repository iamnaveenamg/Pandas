import pandas as pd
import numpy as np

df = pd.DataFrame({
    'Name': ['John', 'Jane', 'Unknown', 'Bob'],
    'City': ['NYC', 'LA', 'NYC', 'Unknown'],
    'Age': [25, 28, 30, 'Unknown']
})

print("Original DataFrame:")
print(df)

# Replace values
print("\nReplace 'Unknown' with NaN:")
df_cleaned = df.replace('Unknown', np.nan)
print(df_cleaned)

# Replace multiple values
df2 = pd.DataFrame({
    'Size': ['Small', 'Medium', 'Large', 'Small'],
    'Status': ['Yes', 'No', 'Yes', 'No']
})

print("\nReplace multiple values:")
df2_cleaned = df2.replace({'Size': {'Small': 'S', 'Medium': 'M', 'Large': 'L'}})
print(df2_cleaned)

# Strip whitespace
df3 = pd.DataFrame({'Name': ['  John  ', 'Jane  ', '  Bob']})
print("\nBefore strip: ")
print(repr(df3['Name']))
df3['Name'] = df3['Name'].str.strip()
print("\nAfter strip:")
print(repr(df3['Name']))
