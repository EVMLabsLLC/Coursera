# why loops
# do not do this:
# print("1")
# print("2")
# print("3")
# print("4")
# print("5")

# # do this instead:
# i = 1
# while i <= 5: # is i less than or equal to 5
#     print(i)
#     i = i + 1
# print("Done")

# i = 1
# while i <= 1_000: # for numbers 1000 or greater, use underscore to make it more readable
#     print(i)
#     i = i + 1
# print("Done")

i = 1
while i <= 10:
    print(i * '*') # multiply the asterisk by the value of i i.e if i is 1, one asterisk will be printed, if i is 2, two asterisks will be printed, etc.
    i = i + 1
print("Done")