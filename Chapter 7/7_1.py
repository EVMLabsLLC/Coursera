# #How I did it
# file = input("Enter a file name: ")
# file_handle = open(file)
# content = file_handle.read()
# content = content.upper()
# content = content.rstrip()
# print(content)

#Better way to do it
file = input("Enter a file name: ")
file_handle = open(file)
# print(file_handle)

for line in file_handle:
    print(line.rstrip().upper())


