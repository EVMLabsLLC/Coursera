number = input("Enter a number: ")
try:
    ival = int(number)
except:
    ival = -1
if ival > 0:
    print("Nice Work!")
else:
    print("Not a number!")

