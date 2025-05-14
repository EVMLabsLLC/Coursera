# Chapter 4: Functions and Error Handling

This chapter covers fundamental concepts in Python programming, focusing on functions and error handling.

## Exercise 4.1: Functions and Return Values
**File:** `4_1.py`

This exercise demonstrates several key concepts:

```python
# String manipulation using max() and min()
text = 'Hello World'
print(max(text))  # Returns 'r'
print(min(text))  # Returns ' ' (space)

# Greeting function with language parameter
def greet(lang):
    if lang == 'es':
        return 'Hola'
    elif lang == 'fr':
        return 'Bonjour'
    else:
        return 'Hello'

# Function with return value
def addtwo(a, b):
    added = a + b
    return a  # Note: This is a bug, should return 'added'
```

Key concepts demonstrated:
1. Function definition and parameters
2. Return values
3. String operations with `max()` and `min()`
4. User input handling
5. Conditional logic in functions

## Exercise 4.6: Pay Calculator with Error Handling
**File:** `4_6.py`

This exercise implements a pay calculator with two versions:

```python
def computepay(hours, rate):
    # Calculate regular pay
    if hours <= 40:
        pay = hours * rate
    else:
        # Calculate overtime
        regular_pay = 40 * rate
        overtime_pay = (hours - 40) * (rate * 1.5)
        pay = regular_pay + overtime_pay
    return pay

# Get input from user
try:
    hours = float(input('Enter Hours: '))
    rate = float(input('Enter Rate: '))
    pay = computepay(hours, rate)
    print('Pay:', pay)
except:
    print('Error, please enter numeric input')
```

Key concepts demonstrated:
1. Function implementation for business logic
2. Overtime calculations (time and a half for hours over 40)
3. Type conversion (string to float)
4. Error handling using try-except blocks
5. User input validation

## Learning Outcomes

### 1. Function Definition and Usage
```python
def function_name(parameters):
    # Function body
    return value
```

### 2. Return Values
```python
def calculate_square(x):
    return x * x
```

### 3. Error Handling
```python
try:
    # Code that might raise an error
    result = perform_operation()
except:
    # Handle the error
    print('An error occurred')
```

### 4. Type Conversion
```python
# String to float
value = float(input('Enter a number: '))

# Float to string
text = str(3.14)
``` 