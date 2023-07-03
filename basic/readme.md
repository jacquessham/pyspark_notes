# Basic
We will go over the basic concepts and PySpark setups.

## Basic Concept

### RDD - Resilient Distributed Dataset
RDD is a distributed datasets that consists of records. It is immutable and divided into one or many partitions and distributed as in-memory collections of objects across worker nodes. It is automatically rebuilt on failure and track lineage info to rebuild lost data, instead of replication.

### RDD Operations
<ul>
	<li>Transformation: Perform functions against each element in an RDD and return a new RDD</li>
	<li>Actions: Trigger a computation and return a value to the Spark driver</li>
</ul>

### SparkContext
SparkContext (sc) is a driver program can access Spark.

```
# Create Spark instance
sc = SparkContext(appName='random_name').getOrCreate()
```

### MapReduce
MapReduce allows computations to be parallelized over a cluster, which is a framework plans map tasks to be run on the correct nodes and shuffle data for the reduce function.

## Environments
Coming soon...

## How to run Python script with PySpark on command line?
Use <b>spark-submit</b> to run the Python script:

```
spark-submit some_script.py
```

## First-Day Syntax

```
# Load data
nums = sc.textFile('../Data/nums.csv', 8)
# Convert to integers
nums = rdd.map(lambda x: int(x))
# Filter
nums = nums.filter(lambda x: x > 5)
# Print the RDD
nums.glom().collect()
# Calculate the sum
nums = nums.reduce(x, y: x + y)
```
### Checking Data Distribution

```
# Check the number of partitions
nums.getNumPartitions()
# Convert partitions to array
nums.glom().collect()
```

<br>
<b>glom()</b>: Convert all elements within each partition into a RDD list
<b>collect()</b>: Return the RDD list from glom() to a list

## Reference
Stack Overflow <a href="https://stackoverflow.com/a/48861241">How to run a script in PySpark?</a>