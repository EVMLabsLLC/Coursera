Understanding Regular Expressions
--------------------------------
Regular expressions (regex) are powerful tools for pattern matching and text manipulation. They allow you to:
- Search for specific patterns in text
- Extract information from strings
- Validate input data
- Replace text based on patterns

Key Concepts:
1. Pattern Matching: Regex uses special characters and sequences to define search patterns
2. Metacharacters: Special characters that have specific meanings (e.g., ^, $, ., *)
3. Character Classes: Sets of characters to match (e.g., [a-z], [0-9])
4. Quantifiers: Specify how many times a pattern should match (e.g., *, +, ?)
5. Anchors: Match positions in the string (e.g., ^ for start, $ for end)
6. Groups: Use parentheses () to capture and group parts of the pattern

Common Use Cases:
- Email validation
- Phone number formatting
- URL parsing
- Data extraction from text
- Input sanitization
- Log file analysis

Python's re Module:
The 're' module provides regex functionality in Python with methods like:
- re.search(): Find first match
- re.findall(): Find all matches
- re.match(): Match at start of string
- re.sub(): Replace matches
- re.split(): Split string by pattern

Python Regular Expression Quick Guide

^        Matches the beginning of a line
$        Matches the end of the line
.        Matches any character
\s       Matches whitespace
\S       Matches any non-whitespace character
*        Repeats a character zero or more times
*?       Repeats a character zero or more times 
         (non-greedy)
+        Repeats a character one or more times
+?       Repeats a character one or more times 
         (non-greedy)
[aeiou]  Matches a single character in the listed set
[^XYZ]   Matches a single character not in the listed set
[a-z0-9] The set of characters can include a range
(        Indicates where string extraction is to start
)        Indicates where string extraction is to end

Chapter 11 Files Overview
------------------------

1. 11_1.py
   - Demonstrates basic regular expression usage with file reading
   - Shows how to search for lines starting with 'From:' in a text file
   - Illustrates the use of the '^' anchor for matching start of lines

2. 11_2.py
   - Shows how to extract numbers and patterns from strings using re.findall()
   - Demonstrates pattern matching with character sets [0-9] and [A,E,I,O,U]
   - Includes commented examples of number extraction

3. 11_2_1.py
   - Explains the difference between greedy and non-greedy matching
   - Demonstrates how .+ and .+? behave differently in pattern matching
   - Shows practical examples of both matching approaches

4. 11_2_2.py
   - Focuses on fine-tuning string extraction
   - Shows how to extract email addresses from text
   - Demonstrates the use of capture groups with parentheses

5. 11_2_3.py
   - Empty file, possibly for future exercises or examples

6. helloworld.py
   - Simple test file with a basic print statement
   - Contains "What up coursera!" message
