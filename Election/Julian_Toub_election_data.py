''' 
Name: Julian_Toub_election_data.py

Description: This code creates either an excel sheet or Matplotlib chart with any repeated words and their frequency. 
The code has the option to use either program by commenting or uncommenting. 

Bugs: none found

Features: exports to excel, graphs with Matplotlib 

Sources: https://www.freecodecamp.org/news/sort-dictionary-by-value-in-python/, 
https://stackoverflow.com/questions/26660654/how-do-i-print-the-key-value-pairs-of-a-dictionary-in-python, 
https://www.geeksforgeeks.org/plot-a-pie-chart-in-python-using-matplotlib/

Log: 1
'''
import string
import numpy as np
import matplotlib.pyplot as plt
counter = 0
terms = []
freq = []
fhand = open('trump.txt')         # Opens the desired txt file, assigns the value fhand to the file. 
counts = dict()                    # Creates an empty dictionary called "counts".
# The for loop iterates through every line of the file (fhand). Creates a variable called line
# which is equal to each line of the text. The trailing white space is removed and the punctuation is omitted.
# Every character is made lowercase. Makes a list called "words" that includes every word as a seperate item. 
for line in fhand:
    line = line.rstrip()
    line = line.translate(line.maketrans("", "", string.punctuation))
    line = line.lower()
    words = line.split()
# Iterates through every word in each line and if the word is equal to one of the words in the
# list below, the code will continue through, if not, the code will add the key and value pair to the
# dictionary "counts" (adds one to the value every time the same word is repeated).
    for word in words:
        if word in ['the','and', 'this', 'that', 'how', 'them', 'an', 'to', 'i', 'about', 'with', 'in', 'am', 'when', 'so', 'who', 'has', 'be', 'going', 'as', 'she', 'he', 'of', 'a', 'for', 'we', 'is', 'my', 'not', 'on', 'our', 'we', 'is', 'have', 'are', 'will', 'it', 'but', 'would', 'was', 'one', 'their', 'what', 'out', 'because', 'at', 'out', 'you', 'by', 'from']:
            continue
        elif word not in counts:
            counts[word] = 1 
        else:
            counts[word] += 1
sorted_dict = dict(sorted(counts.items(), key=lambda x:x[1], reverse=True))     # "sorted_dict" is equal to 
# The sorted version of the dictionary "couts" in decescending order. 
# Creates a csv file called "JT_election_data.csv". This block will reference the variable "counter" that is
# stored at the begining of the program. If the value is >= to 10 and the coutner is <= 15, the key-value pair
# will be written to excel. 
# TO USE EXCEL, MAKE SURE THE CODE BELOW IS UNCOMMENTED AND THE CODE FOR MATPLOTLIB IS COMMENTED OUT
with open('JT_election_data.csv', 'w', newline='') as file:
    for key, value in sorted_dict.items():
        if value >= 10 and counter <= 15:
            counter += 1
            file.writelines(key + ',' + str(value) + "\n")
# If the value is >= 10 and counter is <= 15, the key is added to a list called "terms" and the value is added
# to a list called "freq". Then, it creates a chart using Matplotlib. 
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
