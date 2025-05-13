`len` (function) = length - returns length of the string starting at 0
`while` statement = IF the statement is still True, continue to loop
`in` = member of i.e. `for letter in fruit` would mean for each item in the value of fruit, run this loop
When slicing, the second number is on beyond the end of th slice - "up to but not including" i.e. `print(s[0:4])` means print `0123`  

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
