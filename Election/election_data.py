# Sources: https://www.freecodecamp.org/news/sort-dictionary-by-value-in-python/, 
# https://stackoverflow.com/questions/26660654/how-do-i-print-the-key-value-pairs-of-a-dictionary-in-python, 
# https://www.geeksforgeeks.org/plot-a-pie-chart-in-python-using-matplotlib/
import csv
import string
import numpy as np
import matplotlib.pyplot as plt
#opens the desired txt file, assigns the value fhand to the file. 
fhand = open('kamala.txt')
#creates an empty dictionary called "counts".
counts = dict()
#iterates through every line of the file (fhand). Creates a variable called line
# which is equal to each line of the text. **** WHAT IS RSTRIP ****
for line in fhand:
    line = line.rstrip()
    line = line.translate(line.maketrans("", "", string.punctuation))
    line = line.lower()
    words = line.split()
#iterates through every word in each line and if the word is equal to one of the words in the
# list below, the code will continue through.  
####
    for word in words:
        if word in ['the','and', 'this', 'that', 'how', 'them', 'an', 'to', 'i', 'about', 'with', 'in', 'am', 'when', 'so', 'who', 'has', 'be', 'going', 'as', 'she', 'he', 'of', 'a', 'for', 'we', 'is', 'my', 'not', 'on', 'our', 'we', 'is', 'have', 'are', 'will', 'it', 'but', 'would', 'was', 'one', 'their', 'what', 'out', 'because', 'at', 'out', 'you', 'by', 'from']:
            continue
        elif word not in counts:
            counts[word] = 1 
        else:
            counts[word] += 1
sorted_dict = counts[word]
sorted_dict = dict(sorted(counts.items(), key=lambda x:x[1], reverse=True))
# TO USE EXCEL, MAKE SURE THE CODE BELOW IS UNCOMMENTED AND THE CODE FOR MATPLOTLIB IS COMMENTED
counter = 0
terms = []
freq = []
with open('election_data.csv', 'w', newline='') as file:
    for key, value in sorted_dict.items():
        if value >= 10 and counter <= 15:
            counter += 1
            terms.append(key)
            freq.append(value)
            file.writelines(key + ',' + str(value) + "\n")




# TO USE MATPLOTLIB, UNCOMMENT THE BELOW SECTION AND COMMENT OUT THE PREVIOUS ONE
# for key, value in sorted_dict.items():
#     if value >= 10 and counter <= 15:
#         counter += 1
#         terms.append(key)
#         freq.append(value)
#             #file.writelines(key + ',' + str(value) + "\n")

# fig = plt.figure(figsize=(10, 7))
# plt.pie(freq, labels=terms)
# plt.show()
