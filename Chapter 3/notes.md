# Chapter 3: Conditional Execution and Error Handling

This chapter focuses on implementing conditional logic and error handling in Python programs. The exercises demonstrate the use of if-else statements, try-except blocks, and input validation.

## Exercise 3.1: Pay Calculator with Overtime
**File:** `3_1.py`

This program calculates employee pay including overtime compensation. It demonstrates:
- User input handling
- Type conversion (string to float)
- Error handling with try-except blocks
- Conditional logic for overtime calculations
- Basic arithmetic operations

Key concepts:
- Input validation using try-except
- Overtime pay calculation (1.5x rate)
- Conditional logic for different pay scenarios
- Proper error messaging

## Exercise 3.2: Grade Calculator
**File:** `3_2.py`

This program converts numerical scores to letter grades. It demonstrates:
- Input validation
- Range checking
- Multiple conditional statements (if-elif-else)
- Error handling for invalid inputs

Key concepts:
- Score validation (must be between 0.0 and 1.0)
- Grade boundaries:
  - A: ≥ 0.9
  - B: ≥ 0.8
  - C: ≥ 0.7
  - D: ≥ 0.6
  - F: < 0.6
- Error handling for invalid inputs
- Multiple condition checking with elif statements

## Common Patterns Used
1. **Input Validation**
   - Using try-except blocks to handle invalid input
   - Converting string input to appropriate numeric types
   - Checking input ranges

2. **Conditional Logic**
   - if-else statements for binary decisions
   - if-elif-else chains for multiple conditions
   - Logical operators for complex conditions

3. **Error Handling**
   - Graceful error messages
   - Program termination on invalid input
   - Input range validation

4. **User Interaction**
   - Clear input prompts
   - Informative error messages
   - Structured output formatting 