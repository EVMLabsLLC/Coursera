#For loop
# numbers = [1, 2, 3, 4, 5]
# print(numbers)

numbers = [1, 2, 3, 4, 5]
for item in numbers:
    print(item) # shows each item on a new line

# why loop dont really need to do this, too much code
i = 0
while i < len(numbers):
    print(numbers[i])
    i = i + 1
    