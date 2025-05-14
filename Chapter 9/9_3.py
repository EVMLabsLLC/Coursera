# #We define the dictionary as counts, and empty dictionary
# counts = dict()
# #We prompt the user to enter a line of text
# print('Enter a line of text:')
# #We then assign the line of text to the variable line
# line = input('')
# #We then split the line of text into words
# words = line.split()

# print('Words:' , words)

# print('Counting...')
# #We then say, for each word in the list of words, we are getting the word and adding 1 to it
# for word in words:
#     #We then say, for each word in the list of words, we are getting the word and adding 1 to it
#     counts[word] = counts.get(word,0) + 1
# #Finally, we print the dictionary
# print('Counts', counts)

# #Looping through dictionaries
# #We define the dictionary as counts, and empty dictionary
# counts = {'chuck': 1, 'fred': 42, 'jan': 100}
# #We then say, for each key in the dictionary, we are getting the key and the value
# for key in counts:
#     #We then print the key and the value
#     print(key, counts[key])

# #Two iteration variables
# #We define the dictionary as data
# data = {'chuck': 1, 'fred': 42, 'jan': 100}
# #We then say, for each key and value in the dictionary, we are getting the key and the value
# for keys,values in data.items() :
#     #We then print the key and the value
#     print(keys, values)

#Circlin back to exaple chuck showed in chapter 1
# We ask the user for a file name
name = input('Enter file name:')
#We handle the file opening here
handle = open(name)
#We define the dictionary as counts, and empty dictionary
counts = dict()
#We then say, for each line in the file
for line in handle:
    #We spilt the line into words
    words = line.split()
    #For each word in the line,
    for word in words:
        #We count the word, and add it to the dictionary, looping through and adding 1 for each time we see that word
        counts[word] = counts.get(word,0) + 1

# #We then print the dictionary
# print(counts)

#Here we set the variable for the number of times the larget word appears
bigcount = None
#Here we set the variable for the word that appears the most
bigword = None
#We then say, for each word and count in the dictionary,
for word,count in counts.items():
    #If the count is greater than the bigcount, or bigcount is none,
    if bigcount is None or count > bigcount:
        #Then we set the word to the bigword
        bigword = word
        #Then we set the count to the bigcount
        bigcount = count
#Finally, we print the word that appears the most and the number of times it appears
print(bigword, bigcount)
