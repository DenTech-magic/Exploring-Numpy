import numpy as np

# Load the raw numbers directly from the CSV column into a 1-Dimensional NumPy array
# This skips the header text row and isolates the raw numeric temperature column
temperatures = np.loadtxt('time_series_data.csv', delimiter=',', skiprows=1, usecols=2)

# Check the total count of elements inside the array
total_readings = temperatures.size

# Check the structural layout (dimensions) of the array
array_shape = temperatures.shape


# PART 2: BASIC DESCRIPTIVE STATISTICS


# Check the array from start to finish to find the highest value
max_val = np.max(temperatures)

# Check the array from start to finish to find the lowest value
min_val = np.min(temperatures)

# Calculate the arithmetic average of all the numbers in the array
mean_val = np.mean(temperatures)

# Find the exact middle value where half the dataset is higher and half is lower
median_val = np.median(temperatures)

# Compute the standard deviation to see how much the numbers spread out from the average
spread_val = np.std(temperatures)

# PART 3: SCALING AND MATHEMATICAL TRANSFORMS (VECTORIZATION)

# Apply a standard formula to the entire array at once to change Celsius to Fahrenheit
fahrenheit_array = (temperatures * 9/5) + 32

# Smooth out the data by rounding every decimal point in the array to one decimal place
rounded_array = np.round(temperatures, decimals=1)

# PART 4: CONDITIONAL FILTERING AND LOGICAL MASKS

# Generate a true/false matrix checking where temperatures climb above 30 degrees
high_temp_mask = temperatures > 30

# Count the total number of entries that met the true condition above 30 degrees
hot_days_count = np.sum(high_temp_mask)

# Isolate the exact positional index coordinates where the values exceed 30 degrees
hot_day_positions = np.where(temperatures > 30)[0]

# Extract only the numbers that match the true criteria into a separate, smaller array
hot_temperatures_only = temperatures[high_temp_mask]

# PART 5: TIME-SERIES SEQUENTIAL ANALYSIS

# Calculate sequential differences by subtracting each array item from the one following it
day_to_day_changes = np.diff(temperatures)

# Find the single sharpest twenty-four-hour temperature jump in the dataset
biggest_positive_shift = np.max(day_to_day_changes)

# PART 6: CONSOLE LOG OUTPUTS

# Print basic information about the array's size and shape
print("--- Array Properties ---")
print("Total Dataset Count:", total_readings)
print("Array Dimensions:", array_shape)

# Print the basic summary statistics
print("\n--- Summary Statistics ---")
print("Maximum Temperature:", round(max_val, 2), "°C")
print("Minimum Temperature:", round(min_val, 2), "°C")
print("Average Temperature:", round(mean_val, 2), "°C")
print("Median Temperature:", round(median_val, 2), "°C")
print("Standard Deviation:", round(spread_val, 2))

# Print the filtering and conditional results
print("\n--- Conditional Threshold Analysis ---")
print(f"Number of Days Exceeding 30°C: {hot_days_count} days")
print("First 5 Index Locations of Hot Days:", hot_day_positions[:5])
print("First 5 Actual Values of Hot Days:", np.round(hot_temperatures_only[:5], 2))

# Print samples of vectorization and sequential tracking
print("\n--- Vector Transformation & Sequential Samples ---")
print("First 3 Elements Converted to Fahrenheit:", np.round(fahrenheit_array[:3], 2))
print("First 3 Day-to-Day Sequential Shifts:", np.round(day_to_day_changes[:3], 2))
print("Maximum Single-Day Positive Temperature Jump:", round(biggest_positive_shift, 2), "°C")
