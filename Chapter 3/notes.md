# Chapter 3: Conditional Execution and Error Handling

This chapter focuses on implementing conditional logic and error handling in Python programs. The exercises demonstrate the use of if-else statements, try-except blocks, and input validation.

## Exercise 3.1: Pay Calculator with Overtime
**File:** `3_1.py`

This program calculates employee pay including overtime compensation:

```python
# Get hours and rate from user
hours = input('Enter Hours: ')
rate = input('Enter Rate: ')

try:
    # Convert inputs to float
    hours = float(hours)
    rate = float(rate)
    
    # Calculate pay
    if hours > 40:
        # Overtime calculation
        regular_pay = 40 * rate
        overtime_pay = (hours - 40) * (rate * 1.5)
        pay = regular_pay + overtime_pay
    else:
        # Regular pay calculation
        pay = hours * rate
    
    print('Pay:', pay)
except:
    print('Error, please enter numeric input')
```

Key concepts demonstrated:
1. User input handling
2. Type conversion (string to float)
3. Error handling with try-except blocks
4. Conditional logic for overtime calculations
5. Basic arithmetic operations

## Exercise 3.2: Grade Calculator
**File:** `3_2.py`

This program converts numerical scores to letter grades:

```python
# Get score from user
score = input('Enter score: ')

try:
    # Convert input to float
    score = float(score)
    
    # Validate score range
    if score < 0.0 or score > 1.0:
        print('Bad score')
    else:
        # Determine grade
        if score >= 0.9:
            print('A')
        elif score >= 0.8:
            print('B')
        elif score >= 0.7:
            print('C')
        elif score >= 0.6:
            print('D')
        else:
            print('F')
except:
    print('Bad score')
```

Key concepts demonstrated:
1. Input validation
2. Range checking
3. Multiple conditional statements (if-elif-else)
4. Error handling for invalid inputs

## Common Patterns Used

### 1. Input Validation
```python
try:
    value = float(input('Enter a number: '))
except:
    print('Error: Please enter a valid number')
```

### 2. Conditional Logic
```python
if condition:
    # Do something
elif another_condition:
    # Do something else
else:
    # Default action
```

### 3. Error Handling
```python
try:
    # Risky operation
    result = perform_operation()
except:
    # Handle error
    print('Error occurred')
```

### 4. User Interaction
```python
# Clear input prompt
value = input('Enter a value: ')

# Informative error message
print('Error: Invalid input. Please try again.')

# Structured output
print(f'Result: {result}')
``` 