import numpy as np
import pandas as pd
import time

"""
1.Use copy=False when possible to avoid unnecessary copies
2. Use categorical data for repeated strings
3. Use inplace=True for memory efficiency
4. Vectorize operations instead of loops
5. Use query() for faster filtering on large datasets
    
"""

# Create large dataset
df_large = pd.DataFrame({
    'ID': range(100000),
    'Value': np.random.randint(1, 1000, 100000)
})

# Loop method (slow)
start = time.time()
result_loop = [x * 2 for x in df_large['Value']]
time_loop = time.time() - start

# Vectorized method (fast)
start = time.time()
result_vec = df_large['Value'] * 2
time_vec = time.time() - start

print(f"Loop time: {time_loop:.6f}s")
print(f"Vectorized time: {time_vec:.6f}s")
print(f"Speedup: {time_loop/time_vec:.0f}x faster!")

# Using query for filtering
start = time.time()
df_filtered_loop = df_large[df_large['Value'] > 500]
time_filter1 = time.time() - start

start = time.time()
df_filtered_query = df_large.query('Value > 500')
time_filter2 = time.time() - start

print(f"\nFilter with boolean: {time_filter1:.6f}s")
print(f"Filter with query: {time_filter2:.6f}s")
     


