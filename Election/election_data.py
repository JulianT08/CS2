#Sources: https://www.freecodecamp.org/news/sort-dictionary-by-value-in-python/

import string

fhand = open('kamala.txt')
counts = dict()

for line in fhand:
    line = line.rstrip()
    # First two parameters are empty strings
    #line = line.translate(line.maketrans("", "", string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
        if word in ['the','and', 'this', 'that', 'how', 'them', 'an', 'to', 'i', 'about', 'with', 'in', 'am', 'when', 'so', 'who', 'has', 'be', 'going', 'as', 'she', 'he', 'of', 'a', 'for', 'we', 'is', 'my', 'not', 'on', 'our', 'we', 'is', 'have']:
            continue
        elif word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1
sorted_dict = counts[word]
sorted_dict = sorted(counts.items(), key=lambda x:x[1], reverse=True)
converted_dict = dict(sorted_dict)
print(converted_dict)
