#source: https://www.geeksforgeeks.org/python-using-2d-arrays-lists-the-right-way/
import random
""" welcome
create 3x3 box
set each box equal to a number (1,2,3, etc.)
ask user to play 2 players or against computor
user = x
bot = o
first = random.choice(user, bot)
print(first goes first)
 """

def board_print(board):
    for row in range(len(board)):
        for col in range(len(board[row])):
            print(board[row][col], end=' ')
        print()
    
board = [[0,1,2],
         [3,4,5],
         [6,7,8]]
board_print(board)
moves = 0
user = 'X'
bot = 'O'
print('''User = X
Bot = O''')
#random_num = random.randint(0,1)
random_num = 0
if random_num == 0:
    while moves < 9:
        rowuser = int(input('Row:  '))
        coluser = int(input('Col:  '))
        board[rowuser][coluser] = 'X'
        board_print(board)


#else:
#    random_num = bot

'''
 
moves = 0
while moves <= 9:
    print box  
    choose a box (ex. 2,0) 
    if box is empty:
        box = x
else;
bot choose a box
outside point = [0, 2]
bot move = [random outside point], [random outside point]
user type move
if x in row [0]:
    row[0] =  '''
