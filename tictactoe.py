#source: https://www.geeksforgeeks.org/python-using-2d-arrays-lists-the-right-way/
import random
import sys
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
def moveuser():
    rowuser = int(input('ROW:  '))
    coluser = int(input('COL:  '))
    return rowuser, coluser
def botmove(board):
    while True:
        rowbot = random.randint(0,2)
        colbot = random.randint(0,2)
        if "X" not in str(board[rowbot][colbot]):
            return rowbot, colbot
def checkwin(board):
    if board[0][0]=="X" and board[0][1]=="X" and board[0][2]=="X":
        print("GAME HAS BEEN WON BY THE USER \n")
        sys.exit()
    elif board[1][0]=="X" and board[1][1]=="X" and board[1][2]=="X":
        print("GAME HAS BEEN WON BY THE USER \n")
        sys.exit()
    elif board[2][0]=="X" and board[2][1]=="X" and board[2][2]=="X":
        print("GAME HAS BEEN WON BY THE USER \n")
        sys.exit()
    elif board[0][0]=="X" and board[1][1]=="X" and board[2][2]=="X":
        print("GAME HAS BEEN WON BY THE USER \n")
        sys.exit()
    elif board[2][0]=="X" and board[1][1]=="X" and board[0][2]=="X":
        print("GAME HAS BEEN WON BY THE USER \n")
        sys.exit()
    elif board[0][0]=="X" and board[1][0]=="X" and board[2][0]=="X":
        print("GAME HAS BEEN WON BY THE USER \n")
        sys.exit()
    elif board[0][1]=="X" and board[1][1]=="X" and board[2][1]=="X":
        print("GAME HAS BEEN WON BY THE USER \n")
        sys.exit()
    elif board[0][2]=="X" and board[1][2]=="X" and board[2][2]=="X":
        print("GAME HAS BEEN WON BY THE USER \n")
        sys.exit()
    elif board[0][0]=="O" and board[0][1]=="O" and board[0][2]=="O":
        print("GAME HAS BEEN WON BY THE USER \n")
        sys.exit()
    elif board[1][0]=="O" and board[1][1]=="O" and board[1][2]=="O":
        print("GAME HAS BEEN WON BY THE USER \n")
        sys.exit()
    elif board[2][0]=="O" and board[2][1]=="O" and board[2][2]=="O":
        print("GAME HAS BEEN WON BY THE USER \n")
        sys.exit()
    elif board[0][0]=="O" and board[1][1]=="O" and board[2][2]=="O":
        print("GAME HAS BEEN WON BY THE USER \n")
        sys.exit()
    elif board[2][0]=="O" and board[1][1]=="O" and board[0][2]=="O":
        print("GAME HAS BEEN WON BY THE USER \n")
        sys.exit()                       
    elif board[0][0]=="O" and board[0][1]=="O" and board[0][2]=="O":
        print("GAME HAS BEEN WON BY THE USER \n")
        sys.exit()
    elif board[1][0]=="O" and board[1][1]=="O" and board[1][2]=="O":
        print("GAME HAS BEEN WON BY THE USER \n")
        sys.exit()
    elif board[2][0]=="O" and board[2][1]=="O" and board[2][2]=="O":
        print('''
        GAME HAS BEEN WON BY THE USER 
        ''')
        sys.exit()                       

def main():
    board = [[0,1,2],
         [3,4,5],
         [6,7,8]]
    board_print(board)
    moves = 0
    print('''User = X
Bot = O''')
    #random_num = random.randint(0,1)
    random_num = 0
    if random_num == 0:
        while moves < 4:
            #move = moveuser(rowuser, coluser)
            rowuser,coluser = moveuser()
            board[rowuser][coluser] = 'X'
            board_print(board)
            rowbot, colbot = botmove(board)
            board[rowbot][colbot] = "O"
            print("\n NOW THE BOT WILL MOVE: ")
            board_print(board)
            checkwin(board)
            moves += 1
if __name__ == "__main__":
    main()
