#source: https://www.geeksforgeeks.org/python-using-2d-arrays-lists-the-right-way/
import random
import sys
import time
def board_print(board):
    for row in range(len(board)):
        for col in range(len(board[row])):
            print(board[row][col], end=' ')
        print()
"""
Prints the board by iterating through the length of it (3x3).

Args:
    board (list): A list of the 3 rows.

Returns:
    Prints the board item by item.

Raises:
    none
"""
def moveuser(board):
    rowuser = int(input('ROW:  '))
    coluser = int(input('COL:  '))
    while str(board[rowuser][coluser]) == "X" or str(board[rowuser][coluser]) == "O":
        print('''
Make sure that you are not attempting to place your move on top of opponents move or your own move. ''')
        rowuser = int(input('ROW:  '))
        coluser = int(input('COL:  '))
    return rowuser, coluser

"""
Promps the user for the row and colomn for their move.

Args:
    none

Returns:
    rowuser(int): The row for the user's move.
    coluser(int): The column for the user's move.

Raises:
    none
"""
def botmove(board):
    while True:
        rowbot = random.randint(0,2)
        colbot = random.randint(0,2)
        while str(board[rowbot][colbot]) == "X" or str(board[rowbot][colbot]) == "O":
            rowbot = random.randint(0,2)
            colbot = random.randint(0,2)

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
        print("GAME HAS BEEN WON BY THE BOT \n")
        sys.exit()
    elif board[1][0]=="O" and board[1][1]=="O" and board[1][2]=="O":
        print("GAME HAS BEEN WON BY THE BOT \n")
        sys.exit()
    elif board[2][0]=="O" and board[2][1]=="O" and board[2][2]=="O":
        print("GAME HAS BEEN WON BY THE BOT \n")
        sys.exit()
    elif board[0][0]=="O" and board[1][1]=="O" and board[2][2]=="O":
        print("GAME HAS BEEN WON BY THE BOT \n")
        sys.exit()
    elif board[2][0]=="O" and board[1][1]=="O" and board[0][2]=="O":
        print("GAME HAS BEEN WON BY THE BOT \n")
        sys.exit()                       
    elif board[0][0]=="O" and board[0][1]=="O" and board[0][2]=="O":
        print("GAME HAS BEEN WON BY THE BOT \n")
        sys.exit()
    elif board[1][0]=="O" and board[1][1]=="O" and board[1][2]=="O":
        print("GAME HAS BEEN WON BY THE BOT \n")
        sys.exit()
    elif board[2][0]=="O" and board[2][1]=="O" and board[2][2]=="O":
        print("GAME HAS BEEN WON BY THE BOT")
        sys.exit()                       

def main():
    board = [[0,1,2],
         [3,4,5],
         [6,7,8]]
    moves = 0
    print('''
User = X
Bot = O''')
    random_num = random.randint(1,2)
    if random_num == 1:
        while moves < 5:
            #move = moveuser(rowuser, coluser)
            board_print(board)
            rowuser,coluser = moveuser(board)
            board[rowuser][coluser] = 'X'
            board_print(board)
            rowbot, colbot = botmove(board)
            board[rowbot][colbot] = "O"
            print("\n NOW THE BOT WILL MOVE: ")
            board_print(board)
            print()
            checkwin(board)
            moves += 1
    else:
        print('''
Welcome to the Tic Tac Toe game! You will be playing against a robot. Randomly, the starter has been assigned as BOT.''')
        time.sleep(3)
        while moves < 5:
            board_print(board)
            rowbot, colbot = botmove(board)
            board[rowbot][colbot] = "O"
            print("\n NOW THE BOT WILL MOVE: ")
            board_print(board)
            print('''
Now you will move.''')
            rowuser,coluser = moveuser(board)
            board[rowuser][coluser] = 'X'
            board_print(board)
            checkwin(board)
            moves += 1


if __name__ == "__main__":
    main()
