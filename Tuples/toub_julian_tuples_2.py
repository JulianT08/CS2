'''
Name: toub_julian_tuples_2.py

Sources: https://github.com/jmelahman/python-for-everybody-solutions/blob/master/exercise10_2.py 
    - Used to understand the framework of the program and then modified to be my own.

Log: 1.0
'''

hours = dict()
table = list()

fname = input("File name: ")
fhand = open(fname)
for line in fhand:
    words = line.split()
    if len(words) < 5 or words[0] != 'From':
        continue
    col_pos = words[5].find(':')
    hour = words[5][:col_pos]
    if hour not in hours:
        hours[hour] = 1      
    else:
        hour[hour] += 1  

for key, val in list(hour.items()):
    table.append((key, val))             

table.sort()                            

for key, val in table:
    print(key, val)