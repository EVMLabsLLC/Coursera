# This program reads a text file containing email headers and calculates the average spam confidence score
# It specifically looks for lines starting with "X-DSPAM-Confidence:" and extracts the numerical values

# Prompt the user to enter the name of the file to process
fname = input("Enter file name: ")

# Open the specified file and create a file handle object to read from it
file_handle = open(fname)

# Initialize variables to keep track of the sum and count of spam confidence scores
total = 0  # Will store the sum of all spam confidence scores
count = 0  # Will keep track of how many spam confidence scores we find

# Loop through each line in the file
for line in file_handle:
    # Skip lines that don't start with "X-DSPAM-Confidence:"
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    
    # Increment the counter for each spam confidence score found
    count = count + 1
    
    # Extract the numerical value from the line (positions 20-26) and add it to the total
    # The format is typically "X-DSPAM-Confidence: 0.8475" where the number starts at position 20
    total = total + float(line[20:26])

# Calculate and print the average spam confidence score
print("Average spam confidence:", total/count)