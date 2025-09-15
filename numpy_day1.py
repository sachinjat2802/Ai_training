import numpy as np

# Create a NumPy array of prices
prices = np.array([1200, 25, 75, 1250, 300, 27, 50, 80, 1200])

# Display the array
print("Prices Array:")
print(prices)

# Accessing elements
print(f"First element: {prices[0]}")
print(f"Last element: {prices[-1]}")
print(f"First 5 elements: {prices[:5]}")
print(f"Last 3 elements: {prices[-3:]}")
print(f"Elements at positions 2, 4, and 6: {prices[[2, 4, 6]]}")
print(f"Elements from position 3 to 7: {prices[3:8]}")

# Statistical summary
print("\nStatistical Summary:")
print(f"Mean Price: {np.mean(prices)}")
print(f"Median Price: {np.median(prices)}")
print(f"Standard Deviation of Prices: {np.std(prices)}")
print(f"Variance of Prices: {np.var(prices)}")
print(f"Minimum Price: {np.min(prices)}")
print(f"Maximum Price: {np.max(prices)}")

# Unique values and counts
unique_prices, counts = np.unique(prices, return_counts=True)
print(f"\nUnique Prices: {unique_prices}")
print(f"Count of Unique Prices: {counts}")

# Sorting
sorted_prices = np.sort(prices)
print(f"\nPrices sorted in ascending order: {sorted_prices}")
sorted_prices_desc = np.sort(prices)[::-1]
print(f"Prices sorted in descending order: {sorted_prices_desc}")

# Filtering
print(f"\nPrices greater than 100: {prices[prices > 100]}")
print(f"Prices between 50 and 300: {prices[(prices >= 50) & (prices <= 300)]}")
print(f"Prices that are either 25 or 300: {prices[np.isin(prices, [25, 300])]}")

# Applying functions
print(f"\nPrices after applying a 10% discount: {prices * 0.9}")
print(f"Prices rounded to the nearest integer: {np.round(prices)}")
print(f"Prices squared: {np.square(prices)}")

