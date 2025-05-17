#Fine-Tuning String Extraction

# Import the regular expression module
import re

# Define a sample string
x = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'

# Use re.findall() to extract the domain name from the email address
# The pattern 'From .*@([^ ]*)' breaks down as follows:
#   - 'From' matches the literal text "From "
#   - .* matches any characters (except newline) zero or more times
y = re.findall('\S+?@\S+' ,x)

# ^From - Matches any line that starts with "From"
# (\S+@\S+) - Matches the email address
# The parentheses capture the email address as a group
# y = re.findall('^From (\S+@\S+)' ,x)
print(y)