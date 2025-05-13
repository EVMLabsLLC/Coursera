# This is a string containing an email header with sender information and timestamp
data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'

# Find the position of the first period (.) in the string
pos = data.find('.')

# Print a slice of the string starting at the period position and including 3 characters after it
print(data[pos:pos+3])