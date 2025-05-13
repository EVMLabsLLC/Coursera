# Get user input for the score
score = input("Enter Score: ")

# Try to convert the input string to a floating-point number
try:
    score = float(score)
except:
    # If conversion fails (e.g., user enters text instead of a number), show error and exit
    print("Error, please enter a numerical value, must be between 0.0 and 1.0")
    quit()

# Check if score is above maximum allowed value (1.0)
if score >= 1.0:
    print("Error, score must be between 0.0 and 1.0")
    quit()

# Grade calculation logic using if-elif-else structure
# A grade for scores 0.9 and above
if score >= 0.9:
    print("A")
# B grade for scores between 0.8 and 0.9
elif score >= 0.8:
    print("B")
# C grade for scores between 0.7 and 0.8
elif score >= 0.7:
    print("C")
# D grade for scores between 0.6 and 0.7
elif score >= 0.6:
    print("D")
# F grade for scores below 0.6
else:
    print("F")