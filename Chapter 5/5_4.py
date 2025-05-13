# #Loop idioms
# #counting in a loop
# zork = 0
# print("Before", zork)
# for thing in [9, 41, 12, 3, 74, 15]:
#     zork = zork + 1
#     print(zork, thing)
# print("After", zork)

# #Adding in a loop
# total = 0
# print("Before", total)
# for num in [9,12, 23, 14, 234]:
#     total = total + num
#     print(total, num)
# print("After", total)

# #Average in a loop
# count = 0
# sum = 0
# for value in [9, 12, 3, 4, 134]:
#     count = count + 1
#     sum = sum + value
#     print(count, sum, value)
# print("After", count, sum, sum / count)

# #Finding the smallest value - None is a special object that represents the absence of a value and should also be used when finding the largest value
# num = None
# print("Before", num)
# for value in [9, 12, 3, 4, 134]:
#     if num is None: ##is is uses when comparing to None
#         num = value
#     elif value < num :
#         num = value
#     print(num, value)
# print("After", num)

# #Worked exercise
# num = 0
# tot = 0.0
# while True : 
#     sval = input("Enter a number: ")
#     if sval == "done" :
#         break
#     try:
#         fval = float(sval)
#     except:
#         print("Invalid input")
#         continue
#     # print(fval)
#     num = num + 1
#     tot = tot + fval

# # print("All done")
# print(tot, num, tot / num)