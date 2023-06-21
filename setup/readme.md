# Setup

## How to install PySpark
Here are the steps:
<ol>
	<li>Install Homebrew</li>
	<li>Install Java via Homebrew</li>
	<li>Install PySpark via Homebrew</li>
</ol>

### Install Homebrew
Install homebrew with below script on command line:

```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

### Install Java via Homebrew
Install Java with below script on command line:

```
brew install openjdk@11
```

### Install PySpark via Homebrew
Install PySpark with below script on command line:

```
brew install apache-spark
```

## Create Environment
Create an environment with below script on command line:

```
conda create --name env_name python=3.6 -y
```

Once it is created, activate with below script on command line:

```
source activate env_name
```

If you need to check the available environment, use the below script on command line:

```
conda info --envs
```

## Reference
SparkBy{Examples} <a href="https://sparkbyexamples.com/pyspark/how-to-install-pyspark-on-mac/?expand_article=1">How to Install PySpark on Mac in 2022</a>