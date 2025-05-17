# Import the regular expression (re) module which provides support for pattern matching in strings
import re

# Define a string variable 'x' containing text with numbers embedded within it
x = 'My 2 favorite numbers are 19 and 42'

# Use re.findall() to extract all numbers from the string 'x'
# '[0-9]+' is the regular expression pattern where:
#   - [0-9] matches any single digit from 0 to 9
#   - + means "one or more" of the preceding pattern
#   - So [0-9]+ will match one or more consecutive digits
# The result is stored in list 'y'
# y = re.findall('[0-9]+',x)

# Extract all vowels from the string 'x' there are no uppercase vowels so we wil return and empty list
y = re.findall('[A,E,I,O,U]+',x)

# Print the list of extracted numbers
# This will output: ['2', '19', '42']
print(y)