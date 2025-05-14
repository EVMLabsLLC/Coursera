# Chapter 5: Loops and Iterations

This chapter covers various aspects of loops and iterations in Python, including while loops, for loops, and common loop patterns.

## Exercise 5.1: Basic Loop Concepts
**File:** `5_1.py`

This exercise introduces basic loop concepts:

```python
# While loop example
n = 5
while n > 0:
    print(n)
    n = n - 1
print('Blastoff!')

# For loop with list
friends = ['Joseph', 'Glenn', 'Sally']
for friend in friends:
    print('Happy New Year:', friend)
print('Done!')
```

Key concepts demonstrated:
1. While loops and their basic structure
2. Converting while loops to for loops
3. Iterating through lists using for loops
4. Loop termination conditions

## Exercise 5.2: Finding Maximum and Minimum Values
**File:** `5_2.py`

This program finds the largest and smallest numbers from user input:

```python
largest = None
smallest = None

while True:
    num = input('Enter a number: ')
    if num == 'done':
        break
    
    try:
        num = float(num)
        if largest is None or num > largest:
            largest = num
        if smallest is None or num < smallest:
            smallest = num
    except:
        print('Invalid input')
        continue

print('Maximum is', largest)
print('Minimum is', smallest)
```

Key concepts demonstrated:
1. Using None as an initial value
2. Sentinel value for loop termination
3. Error handling for invalid inputs
4. Maintaining running maximum and minimum values

## Exercise 5.3: Finding the Largest Number
**File:** `5_3.py`

This program demonstrates finding the largest number in a list:

```python
numbers = [3, 41, 12, 9, 74, 15]
largest = None

for num in numbers:
    if largest is None or num > largest:
        largest = num
    print('Current number:', num, 'Largest so far:', largest)

print('Largest:', largest)
```

Key concepts demonstrated:
1. Finding maximum values in a list
2. Using None as an initial value
3. Debugging with print statements
4. For loop iteration

## Exercise 5.4: Common Loop Patterns
**File:** `5_4.py`

This exercise demonstrates common loop patterns:

```python
# Counting in a loop
count = 0
for num in [3, 41, 12, 9, 74, 15]:
    count = count + 1
print('Count:', count)

# Summing in a loop
total = 0
for num in [3, 41, 12, 9, 74, 15]:
    total = total + num
print('Sum:', total)

# Finding average
count = 0
sum = 0
for num in [3, 41, 12, 9, 74, 15]:
    count = count + 1
    sum = sum + num
print('Average:', sum/count)

# Finding smallest value
smallest = None
for num in [3, 41, 12, 9, 74, 15]:
    if smallest is None or num < smallest:
        smallest = num
print('Smallest:', smallest)
```

Key concepts demonstrated:
1. Counting in a loop
2. Adding numbers in a loop
3. Calculating averages
4. Finding minimum values
5. Using None as a special value

## Best Practices

### 1. Loop Control
```python
# Break statement
while True:
    if condition:
        break

# Continue statement
for item in items:
    if not condition:
        continue
    # Process item
```

### 2. Error Handling
```python
try:
    value = float(input('Enter a number: '))
except:
    print('Invalid input')
    continue
```

### 3. Variable Initialization
```python
# Initialize before loop
count = 0
total = 0
largest = None
smallest = None
```

### 4. Loop Termination
```python
# Using sentinel value
while True:
    value = input('Enter value (done to quit): ')
    if value == 'done':
        break
``` 