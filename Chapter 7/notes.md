# Chapter 7: Files and File Handling

## Basic File Operations
- File Handle = `open`, `read`, `write`, `close`
- Newline character (`\n`) creates a new line in text files
  Example:
  ```
  Hello\nWorld!
  ```
  Prints:
  ```
  Hello
  World
  ```

## Exercise Files and Their Purposes

### 7_1.py - File Reading and String Manipulation
This exercise demonstrates basic file reading and string manipulation:
- Takes a filename as input from the user
- Opens and reads the file
- Converts all text to uppercase
- Prints each line with proper formatting
- Shows two approaches:
  1. Reading entire file at once
  2. Reading line by line (more memory efficient)

### 7_2.py - Spam Confidence Calculator
This program processes email headers to calculate average spam confidence:
- Reads a file containing email headers
- Looks for lines starting with "X-DSPAM-Confidence:"
- Extracts numerical confidence values
- Calculates and displays the average spam confidence score
- Demonstrates:
  - File iteration
  - String parsing
  - Numerical calculations
  - Error handling

### Supporting Files
- `mbox-short.txt`: Sample email data file used for spam confidence calculations
- `words.txt`: Text file used for file reading exercises

## Key Concepts Covered
1. File Operations
   - Opening files
   - Reading files
   - Processing file contents
   - String manipulation
2. File Iteration
   - Line-by-line processing
   - String methods
   - Data extraction
3. Error Handling
   - File existence checks
   - Data validation
4. String Processing
   - String slicing
   - String methods
   - Case conversion
