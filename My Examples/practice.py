#convert weight to kilos or pounds
weight = float(input("Enter your weight: ")) # here we use float to allow decimal
unit =  input("(L)bs or (K)g: ")
if unit.upper() == "L": # upper converts to uppercase incase users input lower case
    converted = int(weight) * 0.45 # we multiply by 0.45 to convert to kilos
    print(f"You are {converted} kilos")
else:
    converted = int(weight) / 0.45 # we divide by 0.45 to convert to pounds
    print(f"You are {converted} pounds")