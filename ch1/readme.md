# Chapter 1 - I/O, Basic Operations
We will go over the syntax on I/O and Basic Operations.
<br>
Coming soon...

## Loading Data

```
df = sc.textFile(filename, num_partition)
```

### Converting Text

```
# Basic Mapping
df = df.map(lambda x: int(x))
# One-to-many Mapping
df = df.flatMap(lambda line: line.split())
```

```
# df.mapPartitions() # Come back later
```

## Basic Operations

### Basic Math Operations
```
df.count()
df.sum()
df.mean()
df.max()
df.min()
df.variance()
df.stdev()
```

### Transformation Operations

```
df.distinct()
df.union(df2)
df.intersection(df2)
df.subtract(df2)
df.cartesian(df2)
# df.sample()
```

### Actions

```
df.first()
df.take(n) # Return an array with the first n elements of the dataset
df.top(n)
df.countByValue() # Come back later
```

## RDD Operations

```
df.collect() # Return all elements to an array
df.reduce(func)
df.fold(0, func)
df.aggregate(zero, SeqOp, combOp) # Coming back later
```

## Output

```
df.saveAsTextFile(filename)
```