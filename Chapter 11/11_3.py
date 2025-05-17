# Import the regular expression module for pattern matching
import re

# Prompt user to enter a file name and store it
file = input("Enter a file name: ")
# Open the specified file for reading
fileHandle = open(file)

# Initialize an empty list to store numbers found in each line
numbers = []
# Initialize a variable to keep track of the running sum
total = 0

# Iterate through each line in the file
for line in fileHandle:
    # Remove trailing whitespace and newline characters
    line = line.rstrip()
    # Find all sequences of digits in the current line using regex
    numbers = re.findall('[0-9]+', line)
    # Process each number found in the line
    for number in numbers:
        # Convert the string number to an integer
        number = int(number)
        # Add the number to our running total
        total += number

# Print the final sum of all numbers found in the file
print(total)