import pandas as pd
import numpy as np

# Create the data
data = {
    'OrderID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Product': ['Laptop', 'Mouse', 'Keyboard', 'Laptop', 'Monitor', 'Mouse', 'Webcam', 'Keyboard', 'Laptop', 'Unknown'],
    'Category': ['Electronics', 'Electronics', 'Electronics', 'Electronics', 'Electronics', 'Electronics', 'Peripherals', 'Electronics', 'Electronics', 'Miscellaneous'],
    'Price': [1200, 25, 75, 1250, 300, 27, 50, 80, 1200, np.nan], # Added a NaN price for demonstration
    'Quantity': [1, 2, 1, 1, 2, 3, 1, 2, 1, 5],
    'OrderDate': pd.to_datetime(['2025-01-15', '2025-01-15', '2025-01-16', '2025-01-17', '2025-01-17', '2025-01-18', '2025-01-18', '2025-01-19', '2025-01-20', '2025-01-20']),
    'CustomerID': ['C1001', 'C1002', 'C1001', 'C1003', 'C1002', 'C1004', 'C1001', 'C1003', 'C1002', 'C1004']
}

# Create the DataFrame
df = pd.DataFrame(data)

# add new key 'TotalPrice' which is Price * Quantity``
df['TotalPrice'] = df['Price'] * df['Quantity']
#handle nan in 'TotalPrice' and 'price' by filling it with 0
df['TotalPrice'].fillna(0, inplace=True)
df['Price'].fillna(0, inplace=True)

#handle unknown product to remove
df = df[df['Product'] != 'Unknown']

# price series start with 0
prices = pd.Series([0] + df['Price'].tolist())
# remove 0 index
prices = prices[1:]




# Display the DataFrame
print(df)

print("\nPrices Series:")
print(prices)

print(f"Type of the object: {type(prices)}")
print(f"Data type of elements: {prices.dtype}")
print(f"Number of elements: {prices.size}")
print(f"Shape of the Series: {prices.shape}")
print(f"The index of the Series: {prices.index}")
print(f"The underlying data as a NumPy array:\n{prices.values}")
print(f"Does the Series have any missing values? {prices.hasnans}")

#Accessing elements
print(f"First element: {prices.iloc[0]}")
print(f"Last element: {prices.iloc[-1]}")
print(f"First 5 elements:\n{prices.iloc[:5]}")
print(f"Last 3 elements:\n{prices.iloc[-3:]}")
print(f"Elements at positions 2, 4, and 6:\n{prices.iloc[[2, 4, 6]]}")
print(f"Elements from position 3 to 7:\n{prices.iloc[3:8]}")

# Statistical summary
print("\nStatistical Summary:")
print(prices.describe())

print(f"Mean Price: {prices.mean()}")
print(f"Median Price: {prices.median()}")
print(f"Standard Deviation of Prices: {prices.std()}")
print(f"Variance of Prices: {prices.var()}")
print(f"Minimum Price: {prices.min()}")
print(f"Maximum Price: {prices.max()}")

# Unique values and counts
print(f"\nUnique Prices: {prices.unique()}")
print(f"Count of Unique Prices: {prices.nunique()}")
print(f"Value Counts:\n{prices.value_counts()}")

# Sorting
print(f"\nPrices sorted in ascending order:\n{prices.sort_values()}")
print(f"Prices sorted in descending order:\n{prices.sort_values(ascending=False)}")
print(f"Prices sorted by index:\n{prices.sort_index()}")
# Filtering
print(f"\nPrices greater than 100:\n{prices[prices > 100]}")
print(f"Prices between 50 and 300:\n{prices[(prices >= 50) & (prices <= 300)]}")
print(f"Prices that are either 25 or 300:\n{prices[prices.isin([25, 300])]}")
# Applying functions    
print(f"\nPrices after applying a 10% discount:\n{prices.apply(lambda x: x * 0.9)}")
print(f"Prices rounded to the nearest integer:\n{prices.apply(np.round)}")
print(f"Prices squared:\n{prices.apply(np.square)}")
# Cumulative operations
print(f"\nCumulative Sum of Prices:\n{prices.cumsum()}")
print(f"Cumulative Product of Prices:\n{prices.cumprod()}")
print(f"Cumulative Maximum of Prices:\n{prices.cummax()}")
print(f"Cumulative Minimum of Prices:\n{prices.cummin()}")
# Handling missing values
prices_with_nan = prices.copy()
prices_with_nan.iloc[3] = np.nan  # Introduce a NaN value for demonstration
print(f"\nPrices with a NaN value:\n{prices_with_nan}")
print(f"Number of missing values: {prices_with_nan.isna().sum()}")
print(f"Prices after filling NaN with 0:\n{prices_with_nan.fillna(0)}")
print(f"Prices after dropping NaN values:\n{prices_with_nan.dropna()}")
# Vectorized operations
print(f"\nPrices increased by 10:\n{prices + 10}")
print(f"Prices multiplied by 1.1:\n{prices * 1.1}")
print(f"Prices divided by 2:\n{prices / 2}")
# Boolean indexing
print(f"\nBoolean Series indicating prices greater than 100:\n{prices > 100}")
print(f"Prices greater than 100:\n{prices[prices > 100]}")  
print(f"Prices less than or equal to 50:\n{prices[prices <= 50]}")
# Resetting index
reset_prices = prices.reset_index(drop=True)
print(f"\nPrices with reset index:\n{reset_prices}")
# Renaming index
renamed_prices = prices.rename(index=lambda x: f"Item_{x+1}")
print(f"\nPrices with renamed index:\n{renamed_prices}")
# Handling duplicates
duplicated_prices = pd.Series([25, 75, 25, 300, 75, 1200])
print(f"\nDuplicated Prices Series:\n{duplicated_prices}")
print(f"Number of duplicated values: {duplicated_prices.duplicated().sum()}")
print(f"Prices after dropping duplicates:\n{duplicated_prices.drop_duplicates()}")
# String operations (if applicable)
product_names = pd.Series(['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Webcam'])
print(f"\nProduct Names Series:\n{product_names}")
print(f"Product Names in uppercase:\n{product_names.str.upper()}")
print(f"Product Names in lowercase:\n{product_names.str.lower()}")  
print(f"Product Names containing 'top':\n{product_names[product_names.str.contains('top')]}")
print(f"Product Names with length greater than 5:\n{product_names[product_names.str.len() > 5]}")
# Combining Series
additional_prices = pd.Series([15, 45, 60, 150, 25], index=[0, 1, 2, 3, 4])
combined_prices = prices.add(additional_prices, fill_value=0)
print(f"\nCombined Prices Series:\n{combined_prices}")
# Grouping and aggregation (if applicable)
category_prices = pd.Series([1200, 25, 75, 300, 27, 50, 80, 1200], index=['Electronics', 'Electronics', 'Electronics', 'Electronics', 'Electronics', 'Peripherals', 'Electronics', 'Electronics'])
grouped = category_prices.groupby(category_prices.index)
print(f"\nGrouped Prices by Category:\n{grouped.sum()}")
print(f"Mean Price by Category:\n{grouped.mean()}")
print(f"Count of Prices by Category:\n{grouped.count()}")
# DateTime operations (if applicable)
order_dates = pd.Series(pd.to_datetime(['2025-01-15', '2025-01-16', '2025-01-17', '2025-01-18', '2025-01-19', '2025-01-20']), name='OrderDate')
print(f"\nOrder Dates Series:\n{order_dates}")
print(f"Year of Order Dates:\n{order_dates.dt.year}")
print(f"Month of Order Dates:\n{order_dates.dt.month}")
print(f"Day of Order Dates:\n{order_dates.dt.day}")
print(f"Weekday of Order Dates:\n{order_dates.dt.weekday}")
print(f"Quarter of Order Dates:\n{order_dates.dt.quarter}")
# Resampling (if applicable)
resampled = order_dates.dt.to_period('M').value_counts().sort_index()
print(f"\nResampled Order Dates by Month:\n{resampled}")

# Merging Series (if applicable)
series1 = pd.Series([100, 200, 300], index=['A', 'B', 'C'])
series2 = pd.Series([400, 500, 600], index=['B', 'C', 'D'])
merged = series1.combine_first(series2)
print(f"\nMerged Series:\n{merged}")

# Exporting Series to CSV
prices.to_csv('prices_series.csv', index=False)

# Importing Series from CSV
imported_prices = pd.read_csv('prices_series.csv').squeeze("columns")
print(f"\nImported Prices Series:\n{imported_prices}")  

# Note: The above code snippets demonstrate various operations on pandas Series.





