course = "Python Programming"
print(course.upper()) #upper case
print(course.lower()) #lower case
print(course.title()) #title case
print(course.strip()) #removes whitespace from the beginning and end of the string
print(course.find("Pro")) #finds the index of the first occurrence of the substring
print(course.replace("Programming", "Scripting")) #replaces the substring with the new substring
print(course) #original string

#in operator
print("Pro" in course) #checks if the substring is in the string returns true or false
print("Scripting" not in course) #checks if the substring is not in the string returns true or false