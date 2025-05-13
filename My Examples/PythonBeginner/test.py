# 10 is not equal to "10" because 10 is an integer and "10" is a string. Statment not executed, move to next statement
if 10 == "10":
    print("a")
# "bag" is greater than "apple" and "bag" is greater than "cat" statement executed, print b
elif "bag" > "apple" and "bag" > "cat":
      print("b")
# "bag" is not equal to "apple" statement not executed, move to next statement
else:
      print("c")