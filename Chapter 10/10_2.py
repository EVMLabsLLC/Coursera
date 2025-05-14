# Ask user to input the file name
fileName = input('Enter a file name: ')
# Open the file for reading
fileHandle = open(fileName)

# Create an empty dictionary to store the count of emails for each hour
hour_counts = {}  # Dictionary to store hour counts

# Loop through each line in the file
for line in fileHandle:
    # Remove trailing whitespace from the line
    line = line.rstrip()
    # Split the line into words
    words = line.split()
    # Check if the line starts with 'From' and has enough words
    if line.startswith('From') and len(words) > 2:
        # Get the time string (e.g., "09:14:16")
        time = words[5]
        # Split the time string by ':' and take the first element (hour)
        hour = time.split(':')[0]
        # Increment the count for this hour in the dictionary
        # If the hour doesn't exist in dictionary, start with 0
        hour_counts[hour] = hour_counts.get(hour, 0) + 1

# Sort the hours and print the results
# sorted(hour_counts.keys()) gives us a list of hours in ascending order
for hour in sorted(hour_counts.keys()):
    # Print each hour and its corresponding count
    print(f"{hour} {hour_counts[hour]}")



