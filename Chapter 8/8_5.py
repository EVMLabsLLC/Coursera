# Ask user to input the name of the file to process
file_name = input("Enter file name: ")
# Open the specified file for reading
file_handle = open(file_name)

# Initialize empty lists to store email addresses and count occurrences
emails = []
count = []

# Iterate through each line in the file
for line in file_handle:
    # Remove trailing whitespace from the line
    line = line.rstrip()
    # Split the line into words
    words = line.split()
    # Check if line starts with "From" and has more than 2 words
    if line.startswith("From") and len(words) > 2:
        # Add the email address (second word) to emails list
        emails.append(words[1])
        # Add 1 to count list to keep track of occurrences
        count.append(1)
        # Calculate total number of "From" lines
        total = sum(count)

# Print each email address found
for email in emails:
    print(email)
# Print the total count of lines starting with "From"
print("There were", total, "lines in the file with From as the first word")