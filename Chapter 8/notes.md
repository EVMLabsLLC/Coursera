# Chapter 8: Lists and List Operations

This chapter covers lists in Python, including list creation, manipulation, and common list operations.

## Basic List Concepts

### List Creation
```python
# Creating lists
friends = ['Joseph', 'Glenn', 'Sally']
numbers = [1, 2, 3, 4, 5]
mixed = ['red', ['1', '2'], '24']
```

### List Iteration
```python
# Using for loop with lists
friends = ['Joseph', 'Glenn', 'Sally']
for friend in friends:
    print('Happy New Year:', friend)
print('Done!')
```

## String vs List Mutability

### Strings are Immutable
```python
# Strings cannot be changed directly
fruit = 'Banana'
# This would cause an error:
# fruit[0] = 'b'

# Instead, create a new string
fruit = fruit.lower()  # Returns 'banana'
```

### Lists are Mutable
```python
# Lists can be modified
numbers = [2, 14, 26, 41, 63]
print(numbers)  # [2, 14, 26, 41, 63]

# Change an element
numbers[2] = 28
print(numbers)  # [2, 14, 28, 41, 63]
```

## List Operations

### Length and Range
```python
# Get list length
friends = ['Joseph', 'Glenn', 'Sally']
print(len(friends))  # Returns 3

# Using range
print(range(4))  # Returns [0, 1, 2, 3]
print(list(range(len(friends))))  # Returns [0, 1, 2]
```

### List Slicing
```python
# Slicing syntax: [start:end] (end is not included)
numbers = [9, 41, 12, 3, 74, 15]

print(numbers[1:3])  # Returns [41, 12]
print(numbers[:4])   # Returns [9, 41, 12, 3]
print(numbers[3:])   # Returns [3, 74, 15]
print(numbers[:])    # Returns [9, 41, 12, 3, 74, 15]
```

## String to List Conversion

### Using split()
```python
# Basic split
text = 'With three words'
words = text.split()
print(words)  # Returns ['With', 'three', 'words']
print(len(words))  # Returns 3
print(words[0])  # Returns 'With'

# Split on specific character
text = 'first;second;third'
words = text.split(';')
print(words)  # Returns ['first', 'second', 'third']
```

## Common List Methods

### 1. List Modification
```python
# append() - add to end
numbers = [1, 2, 3]
numbers.append(4)  # [1, 2, 3, 4]

# extend() - add multiple items
numbers.extend([5, 6])  # [1, 2, 3, 4, 5, 6]

# insert() - add at specific position
numbers.insert(0, 0)  # [0, 1, 2, 3, 4, 5, 6]
```

### 2. List Removal
```python
# remove() - remove specific value
numbers = [1, 2, 3, 2]
numbers.remove(2)  # [1, 3, 2]

# pop() - remove and return last item
last = numbers.pop()  # Returns 2, numbers is now [1, 3]
```

### 3. List Sorting
```python
# sort() - sort in place
numbers = [3, 1, 4, 2]
numbers.sort()  # [1, 2, 3, 4]

# sorted() - return new sorted list
numbers = [3, 1, 4, 2]
sorted_numbers = sorted(numbers)  # [1, 2, 3, 4]
```

### 4. List Searching
```python
# index() - find position of value
numbers = [1, 2, 3, 2]
pos = numbers.index(2)  # Returns 1

# count() - count occurrences
count = numbers.count(2)  # Returns 2
```
