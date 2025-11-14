import statistics

numbers = [10, 25, 15, 30, 20, 35, 15, 40, 25, 18]

# Calculate statistics
mean = statistics.mean(numbers)
median = statistics.median(numbers)
mode = statistics.mode(numbers)
stdev = statistics.stdev(numbers)
variance = statistics.variance(numbers)
min_val = min(numbers)
max_val = max(numbers)
range_val = max_val - min_val

# Display results
print(f"Numbers: {numbers}")
print(f"Mean: {mean:.2f}")
print(f"Median: {median:.2f}")
print(f"Mode: {mode}")
print(f"Standard Deviation: {stdev:.2f}")
print(f"Variance: {variance:.2f}")
print(f"Minimum: {min_val}")
print(f"Maximum: {max_val}")
print(f"Range: {range_val}")