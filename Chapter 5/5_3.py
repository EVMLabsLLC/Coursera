# Initialize a variable to keep track of the largest number found so far
# Start with -1 as a baseline (assuming we'll find larger numbers in the list)
largest_so_far = -1

# Print the initial value before we start searching
print("Before", largest_so_far)

# Loop through each number in our list
for num in [9, 12, 15, 41, 6, 82, 197, 1, 23, 115, 23453, 34, 4, 2345345, 454]:
    # If the current number is larger than our largest number so far
    if num > largest_so_far:
        # Update our largest number to the current number
        largest_so_far = num
    # Print both the current largest number and the number we just checked
    print(largest_so_far, num)

# Print the final largest number found after checking all numbers
print("After", largest_so_far)