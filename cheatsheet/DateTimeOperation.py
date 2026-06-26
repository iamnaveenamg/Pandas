import pandas as pd
import numpy as np

dates = pd.date_range('2024-01-01', periods=10, freq='D')
data = np.random.randint(100, 200, 10)
df = pd.DataFrame({'Date': dates, 'Sales': data})

print("Time series DataFrame:")
print(df)

# Extract Date components
df['Year']=df['Date'].dt.year
df['Month']=df['Date'].dt.month
df['Day']=df['Date'].dt.day
df['DayOfWeek']=df['Date'].dt.dayofweek

print("\nWith date components:")
print(df[['Date', 'Year', 'Month', 'Day', 'DayOfWeek']].head())

# Set date as index
df_ts=df.set_index('Date')
print('\nWith date Index:')
print(df_ts)

# Resample to weekly
print('\nResampled to Weekly(sum):')
print(df_ts['Sales'].resample('W').sum())

#Rolling Window
print('\n Rolling Mean 3days window')
print(df_ts['Sales'].rolling(window=3).mean())
