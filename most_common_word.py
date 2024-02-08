# This program finds the most common word in a text file


name = input('Enter file:')
handle = open(name,'r')
counts = dict()

for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

bigcount = None
bigword = None
for word, count in list(counts.items()):
    if word == 'of':
        print(bigword, bigcount)
        continue
    elif word == 'the':
        print(bigword, bigcount)
        continue  
    elif word == 'and':
        print(bigword, bigcount)
        continue
    elif word == 'is':
        print(bigword, bigcount)
        continue
    else:
        bigcount is None or count > bigcount
        bigword = word
        bigcount = count

print(bigword, bigcount)
