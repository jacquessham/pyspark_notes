from pyspark import SparkContext, SparkConf


# Create Spark instance
sc = SparkContext(appName='basics').getOrCreate()
sc.setLogLevel("OFF") # Turn off the logs on command line
# Read Text file
nums = sc.textFile('../Data/numbers.txt',4)

# Convert data to integer
nums = nums.map(lambda x: int(x))
nums_len = nums.count()
nums_sum = nums.sum()
print(f"There are {nums_len} elements in the file")
print(f"And it sums up to {nums_sum}")

# Filter data less than 5
small_nums = nums.filter(lambda x: x < 5)

# Calculate the sum
small_nums = small_nums.reduce(lambda x, y: x + y)
print(f"After we sum up all small numbers, the result is {small_nums}")

# Filter data to even number, count elements, and sum
odd_nums = nums.filter(lambda x: x % 2 == 0)
odd_nums = odd_nums.aggregate((0,0),
                              (lambda x, y: (x[0] + 1, x[1] + y)),
                              (lambda x, y: (x[0] + y[0], x[1] + y[1])))
print(f"The odd numbers are sum to {odd_nums[1]} with {odd_nums[0]} elements")


# Stop Spark instance
sc.stop()