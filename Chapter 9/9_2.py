# # We define the dictionary as counts, and empty dictionary
# counts = dict()
# # We define the initial list of names
# names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
# # here, we are saying, for each name in the list of names, 
# for name in names :
# #If the name is not in the dictionary, we add it to the dictionary
#     if name not in counts:
# #We then set the count of the name to 1
#         counts[name] = 1
# #Else here, being if the the if statement is faulse, i.e. the name is already in the dictionary
#     else :
# # we then add the add 1 to the count for the name
#         counts[name] = counts[name] + 1
# #Finally, we print the dictionary
# print(counts)

#Simplified counting with get()
counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
#Here, we are saying, for each name in the list of names,
for name in names :
#We are saying, for each name in the list of names, we are getting the name and adding 1 to it
    counts[name ]= counts.get(name, 0) + 1
#Finally, we print the dictionary
print(counts)