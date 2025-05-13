# Ask the user to input a file name and store it in the variable 'fname'
fname = input("Enter file name: ")

# Open the file specified by 'fname' and store the file handle in 'fh'
fh = open(fname)

# Initialize an empty list to store unique words
unique_words = []

# Iterate through each line in the file
for line in fh:
    # Split the current line into a list of words using whitespace as delimiter
    words = line.split()
    # Iterate through each word in the current line
    for word in words:
        # Check if the word is not already in our unique_words list
        if word not in unique_words:
            # If it's a new word, add it to our unique_words list
            unique_words.append(word)

# Sort the list of unique words alphabetically
unique_words.sort()

# Print the sorted list of unique words
print(unique_words)
