# Chapter 6: String Manipulation

This chapter covers string manipulation techniques in Python, including string methods, slicing, and common string operations.

## Key String Concepts

### String Length and Membership
```python
# len() function returns length of string
fruit = 'banana'
print(len(fruit))  # Returns 6

# in operator checks membership
if 'a' in fruit:
    print('Found it!')
```

### String Slicing
```python
# Slicing syntax: [start:end] (end is not included)
s = 'Monty Python'
print(s[0:4])   # Returns 'Mont'
print(s[6:7])   # Returns 'P'
print(s[6:20])  # Returns 'Python'
print(s[:2])    # Returns 'Mo'
print(s[8:])    # Returns 'thon'
print(s[:])     # Returns 'Monty Python'
```

## Exercise 6.1: String Manipulation
**File:** `6_1.py`

This exercise demonstrates string slicing and the `find()` method:

```python
# Working with email data
data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'

# Find position of @ symbol
atpos = data.find('@')
print(atpos)  # Returns 21

# Find position of space after @
sppos = data.find(' ', atpos)
print(sppos)  # Returns 31

# Extract the host
host = data[atpos+1:sppos]
print(host)  # Returns 'uct.ac.za'
```

Key concepts demonstrated:
1. String slicing
2. The `find()` method
3. Working with email header data
4. Extracting specific parts of strings

## Exercise 6.5: Number Extraction
**File:** `6_5.py`

This exercise explores different approaches to extract numbers from strings:

```python
# Method 1: Using find() and slicing
text = 'X-DSPAM-Confidence: 0.8475'
pos = text.find(':')
number = float(text[pos+1:])
print(number)  # Returns 0.8475

# Method 2: Using split()
text = 'X-DSPAM-Confidence: 0.8475'
words = text.split()
number = float(words[1])
print(number)  # Returns 0.8475
```

Key concepts demonstrated:
1. String slicing
2. Type conversion (string to float)
3. Handling whitespace in string data
4. Multiple approaches to solve the same problem

## Common String Methods

### 1. String Search
```python
# find() method
text = 'Hello World'
pos = text.find('World')  # Returns 6
```

### 2. String Case
```python
# Case conversion
text = 'Hello World'
print(text.upper())  # Returns 'HELLO WORLD'
print(text.lower())  # Returns 'hello world'
```

### 3. String Replacement
```python
# replace() method
text = 'Hello World'
new_text = text.replace('World', 'Python')
print(new_text)  # Returns 'Hello Python'
```

### 4. String Stripping
```python
# strip() method
text = '  Hello World  '
print(text.strip())  # Returns 'Hello World'
```

# Chapter 6 Exercises and Concepts

## String Manipulation Exercises

### Exercise 6.1 (6_1.py)
- Demonstrated string slicing and the `find()` method
- Worked with email header data to extract specific parts
- Used `find()` to locate the position of a period (.)
- Applied string slicing to extract characters after the found position

### Exercise 6.5 (6_5.py)
- Explored different approaches to extract and convert floating-point numbers from strings
- Demonstrated three methods:
  1. Using `find()` to locate number position and slice
  2. Finding exact number match in string
  3. Dr. Chuck's robust solution using colon position
- Key concepts:
  - String slicing
  - Type conversion (string to float)
  - Handling whitespace in string data
  - Multiple approaches to solve the same problem

## Key String Methods Used
- `find()`: Locates the position of a substring within a string
- String slicing: Extracts portions of strings using [start:end] notation
- Type conversion: Converting between string and numeric types using `float()`  
