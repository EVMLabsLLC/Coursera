#tuples
#tuples are immutable, meaning they cannot be changed once created
# numbers = (1, 2, 3, 4, 5)
# print(numbers)

numbers = (1, 2, 3, 3) # use parenthese to define a tuple, square brackets to define a list
print(numbers.count(3)) # this will return the number of times the item 3 appears in the tuple
print(numbers.index(3)) # this will return the index of the item 3 in the tuple

#unpacking
coordinates = (1, 2, 3)
x, y, z = coordinates
