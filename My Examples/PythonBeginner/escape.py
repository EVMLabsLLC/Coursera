#similar to markdonw we use \ to escape characters
course = "Python\'s Course for Beginners"
print(course)

#new line
message = "John\nSmith"
print(message)

#tab
message = "John\tSmith"
print(message)

#backslash
message = "John\\Smith"
print(message)

#single quote
message = 'John\'s Course'
print(message)

#double quote
message = "John's Course"
print(message)

#triple quotes
message = """
Hello John,

This is a message from the teacher.

"""
print(message)

#formatted strings
first = "John"
last = "Smith"
message = f"Hello {first} {last}"
print(message)

#string methods
course = "Python for Beginners"
print(course.replace("for Beginners", "for Experts"))
print(course)











