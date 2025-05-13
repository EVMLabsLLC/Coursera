# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# range(1, 10)

# for number in numbers:
#     if number % 2 == 0:
#         print(number)
# print("We have", len(numbers), "even numbers")

#this is what we want to do
count = 0
for number in range(1, 10):
    if number % 2 == 0:
        count += 1
        print(number)
print("We have", count, "even numbers")
