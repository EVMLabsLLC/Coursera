# Original version of the code (commented out)
# Import the regular expression module
# import re
# # Open the file 'mbox-short.txt' and store the file handle in variable 'hand'
# hand = open('mbox-short.txt')
# # Loop through each line in the file
# for line in hand:
#     # Remove trailing whitespace and newline characters from the line
#     line = line.rstrip()
#     # Check if the line contains the pattern 'From:' using regular expressions
#     if re.search('From:', line):
#         # If the pattern is found, print the line
#         print(line)

# Import the regular expression module for pattern matching
import re
# Open the file 'mbox-short.txt' and store the file handle in variable 'hand'
hand = open('mbox-short.txt')
# Loop through each line in the file
for line in hand:
    # Remove trailing whitespace and newline characters from the line
    line = line.rstrip()
    # Search for lines that start with 'From:' using the '^' anchor
    # '^' means the pattern must appear at the start of the line
    # This is more precise than the previous version which would match 'From:' anywhere in the line
    if re.search('^From:', line):
        # If the pattern is found at the start of the line, print the line
        print(line)