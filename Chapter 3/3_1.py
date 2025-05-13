# This program calculates employee pay including overtime
# It takes three inputs: regular hours, overtime hours, and hourly rate
# The program handles both regular pay and overtime pay (1.5x rate for overtime)

# Get user input for hours, overtime, and rate
hours = input("Enter Hours: ")      # Prompt for regular hours worked
overtime = input("Enter Overtime: ") # Prompt for overtime hours worked
rate = input("Enter Rate: ")        # Prompt for hourly rate

# Use try-except block to handle potential input errors
try:
    # Convert string inputs to floating-point numbers
    hours = float(hours)            # Convert hours to float
    overtime = float(overtime)      # Convert overtime to float
    rate = float(rate)              # Convert rate to float
except:
    # If conversion fails (non-numeric input), show error and exit
    print("Error, please enter a numerical value")
    quit()

# Calculate base pay (regular hours × rate)
base_pay = float(hours) * float(rate)

# Calculate overtime pay (overtime hours × rate × 1.5)
overtime_pay = (float(overtime) * float(rate) * 1.5)

# Check if total hours exceed 40 (standard work week)
if float(hours) + float(overtime) > 40:
    # If over 40 hours, print total pay including overtime
    print(base_pay + overtime_pay)
else:
    # If 40 hours or less, print only base pay
    print(base_pay)