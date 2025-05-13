# age should be between 18 and 65
age = 22
if age >= 18 and age < 65:
    print("Eligible")
else:
    print("Not eligible")

#Better way
age = 22
if 18 <= age < 65:
    print("Eligible")