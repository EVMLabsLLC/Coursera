# age = 22
# if age >= 18:
#     print("Eligible")
# else:
#     print("Not eligible")

#Clean code
# age = 22
# if age >= 19:
#     message = "Eligible"
# else:
#     message = "Not eligible"

# print(message)

#Better way
age = 22
message = "Eligible" if age >= 18 else "Not eligible"
print(message)
