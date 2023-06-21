from pyspark import SparkContext, SparkConf


# Create Spark instance
sc = SparkContext(appName='basics').getOrCreate()
# Read Text file
nums = sc.textFile('../Data/numbers.txt',4)

# Convert data to integer
nums = nums.map(lambda x: int(x))

# Filter Data less than 5
nums = nums.filter(lambda x: x < 5)

# Calculate the sum
nums = nums.reduce(lambda x, y: x+y)

# Print result
print(f"The result is {nums}")

# Stop Spark instance
sc.stop()