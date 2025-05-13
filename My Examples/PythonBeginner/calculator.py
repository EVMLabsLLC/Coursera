first_number = float(input("First: "))
action = input("Action: ")
second_number = float(input("Second "))

if action == "+":
    sum = first_number + second_number
    print("Total: " + str(sum))
elif action == "-":
    difference = first_number - second_number
    print("Total: " + str(difference))
elif action == "*":
    product = first_number * second_number
    print("Total: " + str(product))
elif action == "/":
    quotient = first_number / second_number
    print("Total: " + str(quotient))
else:
    print("Invalid action")