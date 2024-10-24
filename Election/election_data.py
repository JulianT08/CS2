#Sources: https://www.freecodecamp.org/news/sort-dictionary-by-value-in-python/, https://stackoverflow.com/questions/26660654/how-do-i-print-the-key-value-pairs-of-a-dictionary-in-python
import csv
import string

fhand = open('kamala.txt')
counts = dict()

for line in fhand:
    line = line.rstrip()
    line = line.translate(line.maketrans("", "", string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
        if word in ['the','and', 'this', 'that', 'how', 'them', 'an', 'to', 'i', 'about', 'with', 'in', 'am', 'when', 'so', 'who', 'has', 'be', 'going', 'as', 'she', 'he', 'of', 'a', 'for', 'we', 'is', 'my', 'not', 'on', 'our', 'we', 'is', 'have', 'are', 'will', 'it', 'but', 'would', 'was', 'one', 'their', 'what', 'out', 'because', 'at', 'out']:
            continue
        elif word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1
sorted_dict = counts[word]
sorted_dict = dict(sorted(counts.items(), key=lambda x:x[1], reverse=True))
for key, value in sorted_dict.items():
    if value >= 10:
        
        print(key + "," +str(value))
    else:
        break
with open('election_data.csv', 'w') as file:
   
    # store the desired header row as a list
    # and store it in a variable
    fieldnames = ['WORD', 'COUNT']
     
    # pass the created csv file and the header
    # rows to the Dictwriter function
    writer = csv.DictWriter(file, fieldnames=fieldnames)
     
    # Now call the writeheader function,
    # this will write the specified rows as
    # headers of the csv file
    for 
    writer.writerows()
