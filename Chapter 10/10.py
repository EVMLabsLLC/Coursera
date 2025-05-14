# # Create a dictionary with key-value pairs
# c = {'a':10, 'b':1, 'c':22}

# # Initialize an empty list to store tuples
# tmp = list()

# # Iterate through dictionary items, creating tuples of (value, key)
# for k, v in c.items() :
#     tmp.append( (v, k) )

# # Print the list of tuples before sorting
# print(tmp)

# # Sort the list in descending order (reverse=True)
# tmp = sorted(tmp, reverse=True)

# # Print the sorted list of tuples
# print(tmp)

# Program to find the 10 most common words in a file
# Get the filename from user input
file = input('Enter a file name: ')

# Open the file for reading
fhand = open(file)

# Initialize an empty dictionary to store word counts
counts = dict()

# Read the file line by line
for line in fhand :
    # Split each line into words
    words = line.split()
    # Count each word's occurrence
    for word in words :
        # Increment the count for each word (default to 0 if word not seen before)
        counts[word] = counts.get(word, 0) + 1

# Create an empty list to store (count, word) tuples
lst = list()

# Convert dictionary to list of tuples
for key, val in counts.items() :
    # Create tuples with count first, then word
    newtup = (val, key)
    lst.append(newtup)

# #shorter version of the above code
# print(sorted( [ (v, k) for k, v in counts.items() ] ))

# Sort the list in descending order by count
lst = sorted(lst, reverse=True)

# Print the top 10 most common words and their counts
for val, key in lst[:10] :
    print(key, val)