file = input('Enter a file name:')
handle = open(file)

counts = dict()

for line in handle:
    line = line.rstrip()
    words = line.split()

    if line.startswith('From') and len(words) > 2:
        email = words[1]
        counts[email] = counts.get(email, 0) + 1

bigcount = None
bigword = None

for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print(bigword, bigcount)