# Chapter 7: Files and File Handling

This chapter covers file operations in Python, including reading, writing, and processing file contents.

## Basic File Operations

### File Handles
```python
# Opening a file
handle = open('filename.txt')

# Reading a file
content = handle.read()

# Closing a file
handle.close()
```

### Newline Character
```python
# The \n character creates a new line
text = 'Hello\nWorld!'
print(text)
# Output:
# Hello
# World!
```

## Exercise 7.1: File Reading and String Manipulation
**File:** `7_1.py`

This exercise demonstrates basic file reading and string manipulation:

```python
# Get filename from user
fname = input('Enter the file name: ')

try:
    # Open and read file
    fhand = open(fname)
    
    # Process each line
    for line in fhand:
        # Convert to uppercase and remove trailing whitespace
        line = line.rstrip().upper()
        print(line)
        
except:
    print('File cannot be opened:', fname)
```

Key concepts demonstrated:
1. File opening and reading
2. Line-by-line processing
3. String manipulation
4. Error handling

## Exercise 7.2: Spam Confidence Calculator
**File:** `7_2.py`

This program processes email headers to calculate average spam confidence:

```python
fname = input('Enter file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

count = 0
total = 0

for line in fhand:
    if line.startswith('X-DSPAM-Confidence:'):
        # Extract confidence value
        pos = line.find(':')
        number = float(line[pos+1:])
        count = count + 1
        total = total + number

if count > 0:
    print('Average spam confidence:', total/count)
```

Key concepts demonstrated:
1. File iteration
2. String parsing
3. Numerical calculations
4. Error handling

## Supporting Files

### mbox-short.txt
Sample email data file used for spam confidence calculations.

### words.txt
Text file used for file reading exercises.

## Key Concepts Covered

### 1. File Operations
```python
# Opening files
handle = open('filename.txt')

# Reading files
content = handle.read()
line = handle.readline()
lines = handle.readlines()

# Processing file contents
for line in handle:
    # Process each line
    print(line.rstrip())
```

### 2. File Iteration
```python
# Line-by-line processing
for line in handle:
    # Remove trailing whitespace
    line = line.rstrip()
    # Skip empty lines
    if len(line) == 0:
        continue
    # Process line
    print(line)
```

### 3. Error Handling
```python
try:
    handle = open('filename.txt')
except:
    print('File cannot be opened')
    exit()
```

### 4. String Processing
```python
# String methods
line = line.rstrip()  # Remove trailing whitespace
line = line.upper()   # Convert to uppercase
line = line.lower()   # Convert to lowercase
```
