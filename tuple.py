'''
Name: toub_julian_tuples_1.py

Sources: https://github.com/jmelahman/python-for-everybody-solutions/blob/master/exercise10_1.py 
    - Used to understand the framework of the program and then modified to be my own.

Log: 1.0
'''

addresses = dict()          
emailcounts = list()

fname = input("File name: ")
fhand = open(fname)
for line in fhand:
    words = line.split()
    if len(words) < 2 or words[0] != 'From':
        continue
    else:
        if words[1] not in addresses:
            addresses[words[1]] = 1       
        else:
            addresses[words[1]] += 1    
for key, val in list(addresses.items()):
    emailcounts.append((val, key))          

emailcounts.sort(reverse=True)                
for count, email in emailcounts[:1]:           
    print(f'Email: {email} Frequency: {count}')
