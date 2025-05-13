# This program calculates gross pay including overtime (time and a half) for hours worked over 40
# First implementation without error handling

# Get user input for hours worked and convert to float
hours = float(input("Enter Hours: "))
# Get user input for hourly rate and convert to float
rate = float(input("Enter Rate: "))

# Define function to compute pay with overtime calculation
def computepay(hours, rate):
    # Check if hours worked exceeds 40 (overtime threshold)
    if hours > 40:
        # Calculate overtime hours (hours worked beyond 40)
        overtime = hours - 40
        # Return total pay: (overtime hours * 1.5 * rate) + (regular hours * rate)
        return overtime * rate * 1.5 + 40 * rate
    else:
        # If no overtime, simply multiply hours by rate
        return hours * rate

# Calculate the pay using the computepay function
pay = computepay(hours, rate)
# Display the calculated pay
print("Pay", pay)

# Second implementation with error handling
# Using try-except to handle non-numeric input gracefully
try:
    # Get user input for hours worked and convert to float
    hours = float(input("Enter Hours: "))
    # Get user input for hourly rate and convert to float
    rate = float(input("Enter Rate: "))
except:
    # If conversion to float fails (non-numeric input), display error message
    print("Error, please enter a numerical value")