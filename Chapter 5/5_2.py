# Initialize variables to store the largest and smallest numbers
# Using None as initial value to handle the first input properly
largest = None
smallest = None

# Start an infinite loop that will continue until user enters "done"
while True:
    # Get input from user
    num = input("Enter a number: ")
    
    # Check if user wants to stop entering numbers
    if num == "done":
        break
    
    # Try to convert the input to an integer
    try:
        fnum = int(num)
    except:
        # If conversion fails, print error and continue to next iteration
        print("Invalid input")
        continue
    
    # Handle the largest number logic
    if largest is None:
        # If this is the first number, set it as largest
        largest = fnum
    elif fnum > largest:
        # If current number is bigger than largest, update largest
        largest = fnum
    
    # Handle the smallest number logic
    if smallest is None:
        # If this is the first number, set it as smallest
        smallest = fnum
    elif fnum < smallest:
        # If current number is smaller than smallest, update smallest
        smallest = fnum

# After loop ends, print the results
print("Maximum is", largest)
print("Minimum is", smallest)