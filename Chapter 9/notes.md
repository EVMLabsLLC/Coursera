# Python Collections and Dictionaries

## Dictionaries
A dictionary is a linear collection of key-value pairs, where you can look up values by their associated "tag" or "key".

### Basic Dictionary Operations
```python
>>> cabinet = dict()
>>> cabinet['summer'] = 12
>>> cabinet['fall'] = 3
>>> cabinet['spring'] = 75
>>> print(cabinet['fall'])
3
>>> cabinet['fall'] = cabinet['fall'] + 2
>>> print(cabinet)
{'summer': 12, 'fall': 5, 'spring': 75}
```

This example demonstrates:
1. Creating an empty dictionary using `dict()`
2. Adding key-value pairs
3. Accessing values using keys
4. Modifying existing values

### Dictionary Initialization
You can create an empty dictionary using either:
```python
>>> cabinet = dict()  # Using dict() constructor
>>> cabinet = {}      # Using curly braces
```

### Basic Counting with Dictionaries
```python
>>> ccc = dict()
>>> ccc['csev'] = 1
>>> ccc['cwen'] = 1
>>> print(ccc)
{'csev': 1, 'cwen': 1}
>>> ccc['cwen'] = ccc['cwen'] + 1
>>> print(ccc)
{'csev': 1, 'cwen': 2}
```

This example shows:
1. Initializing a dictionary
2. Adding initial counts
3. Incrementing existing counts
4. Viewing the updated dictionary

### Dictionary Iteration
There are several ways to iterate through dictionaries:

1. Iterating through keys:
```python
>>> counts = {'chuck': 1, 'fred': 42, 'jan': 100}
>>> for key in counts: 
...     print(key, counts[key])
...
chuck 1
fred 42
jan 100
```

2. Retrieving different views of the dictionary:
```python
>>> jjj = {'chuck': 1, 'fred': 42, 'jan': 100}
>>> print(list(jjj))           # List of keys
['chuck', 'fred', 'jan']
>>> print(list(jjj.keys()))    # Explicit list of keys
['chuck', 'fred', 'jan']
>>> print(list(jjj.values()))  # List of values
[1, 42, 100]
>>> print(list(jjj.items()))   # List of (key, value) tuples
[('chuck', 1), ('fred', 42), ('jan', 100)]
```

### Counting Patterns in Dictionaries

There are two main ways to count occurrences in dictionaries:

1. Using if/else pattern:
```python
counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name] + 1
```

2. Using the get() method (simplified):
```python
counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names:
    counts[name] = counts.get(name, 0) + 1
```

The get() method is more elegant as it handles the case of new keys automatically. If the key doesn't exist, it returns the default value (0 in this case).

### File Word Counting
To count words in a file and find the most common word:

```python
# Ask for file name
name = input('Enter file name:')
handle = open(name)

# Initialize empty dictionary
counts = dict()

# Process each line in the file
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

# Find the most common word
bigcount = None
bigword = None
for word, count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print(bigword, bigcount)
```

This pattern is useful for:
1. Reading files line by line
2. Splitting lines into words
3. Counting word frequencies
4. Finding the maximum value in a dictionary

### Email Address Counting Assignment
This assignment demonstrates how to count email addresses from specific lines in a file:

```python
# Get file name from user
file = input('Enter a file name:')
handle = open(file)

# Initialize counting dictionary
counts = dict()

# Process each line in the file
for line in handle:
    # Remove trailing whitespace
    line = line.rstrip()
    # Split line into words
    words = line.split()

    # Check if line starts with 'From' and has enough words
    if line.startswith('From') and len(words) > 2:
        # Get email address (second word in line)
        email = words[1]
        # Count occurrences of this email
        counts[email] = counts.get(email, 0) + 1

# Find the most frequent email
bigcount = None
bigword = None
for word, count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print(bigword, bigcount)
```

This program demonstrates several important concepts:
1. File handling and line-by-line processing
2. String manipulation with `rstrip()` to remove trailing whitespace
3. Conditional filtering of lines using `startswith()`
4. Array indexing to extract specific words
5. Dictionary counting with the `get()` method
6. Finding the maximum value in a dictionary

The program specifically:
- Reads a file line by line
- Looks for lines that start with 'From'
- Extracts the email address (second word) from those lines
- Counts how many times each email appears
- Finds and prints the email that appears most frequently

This is a common pattern in data analysis where you need to:
1. Filter specific lines from a file
2. Extract particular fields from those lines
3. Count occurrences of those fields
4. Find the most common occurrence

