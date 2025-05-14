# Python Tuples

## Chapter Overview
This chapter focuses on tuples and their practical applications in Python. The chapter includes several example files:

- `notes.md`: This file containing the chapter's documentation and examples
- `10.py`: A program that demonstrates finding the 10 most common words in a text file using tuples and dictionaries
- `10_2.py`: A program that analyzes email timestamps to count emails by hour
- `mbox-short.txt`: A sample email log file used for the email analysis program
- `romeo.txt`: A sample text file used for word counting exercises

## Introduction to Tuples
Tuples are similar to lists but with a key difference - they are immutable. This means once a tuple is created, you cannot modify it by adding, removing, or changing elements.

### Key Characteristics
- Tuples are immutable
- Cannot perform operations like sort, append, extend, or reverse
- More efficient than lists for certain operations

## Tuple Assignment
Tuples can be used for multiple assignment in a single statement:

```python
>>> (x, y) = (4, 'fred')
>>> print(y)
fred
>>> (a, b) = (99, 98)
>>> print(a)
99
```

## Tuple Comparison
When comparing tuples, Python evaluates from left to right, comparing elements in order:

```python
>>> (2, 3, 5) > (1, 3, 4)
True
```

The comparison is true because 2 is greater than 1, and Python stops comparing after finding the first difference.

## Sorting Dictionaries by Values
Tuples are particularly useful when you need to sort a dictionary by its values instead of keys. Here's how to do it:

```python
>>> c = { 'a':10, 'b':1, 'c':22}
>>> tmp = list()
>>> for k, v in c.items():
...     tmp.append((v, k))
...
>>> print(tmp)
[(10, 'a'), (1, 'b'), (22, 'c')]
>>> tmp = sorted(tmp, reverse=True)
>>> print(tmp)
[(22, 'c'), (10, 'a'), (1, 'b')]
```

This pattern is useful when you need to:
1. Convert dictionary items to a list of tuples
2. Sort the tuples based on values
3. Reverse the order to get highest values first
