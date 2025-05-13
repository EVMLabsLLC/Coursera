# number = 100
# while number > 0:
#     print(number)
#     # number = number // 2
#     number //= 2
# print("Done")

# command = ""
# while command.lower() != "quit":
#     command =input(">")
#     print("ECHO", command)

#infinite loop
while True:
    command =input(">")
    print("ECHO", command)
    if command.lower() == "quit":
        break