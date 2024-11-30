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
    board(list): A list of the 3 rows.

Returns:
    Prints the board item by item.

Raises:
    none
"""
def moveuser(board):
    while True:
        userchoice = input("Move: ")
        if userchoice.isdigit() and int(userchoice) <= 9:
            if int(userchoice) == 1 and str(board[0][0]) != "X" and str(board[[0][0]]) != "O":
                board[0][0] = "X"
                return userchoice
            elif int(userchoice) == 2 and str(board[0][1]) != "X" and str(board[0][1]) != "O":
                board[0][1] = "X"
                return userchoice
            elif int(userchoice) == 3 and str(board[0][2]) != "X" and str(board[0][2]) != "O":
                board[0][2] = "X"
                return userchoice
            elif int(userchoice) == 4 and str(board[1][0]) != "X" and str(board[1][0]) != "O":
                board[1][0] = "X"
                return userchoice
            elif int(userchoice) == 5 and str(board[1][1]) != "X" and str(board[1][1]) != "O":
                board[1][1] = "X"
                return userchoice
            elif int(userchoice) == 6 and str(board[1][2]) != "X" and str(board[1][2]) != "O":
                board[1][2] = "X"
                return userchoice
            elif int(userchoice) == 7 and str(board[2][0]) != "X" and str(board[2][0]) != "O":
                board[2][0] = "X"
                return userchoice
            elif int(userchoice) == 8 and str(board[2][1]) != "X" and str(board[2][1]) != "O":
                board[2][1] = "X"
                return userchoice
            elif int(userchoice) == 9 and str(board[2][2]) != "X" and str(board[2][2]) != "O":
                board[2][2] = "X"
                return userchoice
        else:
            print('''
Make sure that you are not attempting to place your move on top of opponents move or your own move. 
AND that your move is a number 1-9. \n''')

"""
Promps the user for the row and colomn for their move. Checks that the move is valid and has not 
already been made. 

Args:
    board(list): A list of the 3 rows.

Returns:
    userchoice(strr): The selected box (1-9) for the user's move.

Raises:
    none
"""
def first_two_botmove(board):
    rows = random.choice([0, 2])
    cols = random.choice([0, 2])
    move = board[rows][cols]    
    while str(board[rows][cols]) == "X" or str(board[rows][cols]) == "O":
        rows = random.choice([0, 2])
        cols = random.choice([0, 2])
        move = board[rows][cols]
    board[rows][cols] = "O"  
    return move
"""
Generates a random corner for the bot to move to. The valid options are any corners spots.

Args:
    board(list): A list of the 3 rows.

Returns:
    move(any): The coordinates for the bot's move.

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
"""
Generates a random place for the bot to move to. 

Args:
    board(list): A list of the 3 rows.

Returns:
    rowbot(int): The generated row (0-2) for the bot's move.
    colbot(int): The generated column (0-2) for the bot's move.

Raises:
    none
"""
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
    board = [[1,2,3],
         [4,5,6],
         [7,8,9]]

    moves = 0
    print('''
User = X
Bot = O''')
    random_num = random.randint(1,2)
    #if the random number is 1, the user will go first
    if random_num == 1:
        while moves <= 8:
            if moves == 0:
                board_print(board)
            moves += 1
            moveuser(board)
            board_print(board)
            checkwin(board)
            if moves <= 2:
                moves += 1
                first_two_botmove(board)
            elif moves == 3 and str(board[1][1]) != "X":
                moves += 1
                board[1][1] = "O"
                print("\n NOW THE BOT WILL MOVE: ")
                board_print(board)
                checkwin(board)
                print('''
Now you will move.''')
                moves += 1
                moveuser(board)
                board_print(board)
                checkwin(board)
            
            else:
                checkwin(board)
                moves += 1
                rowbot, colbot = botmove(board)
                board[rowbot][colbot] = "O"
            print("\n NOW THE BOT WILL MOVE: ")
            time.sleep(1)
            board_print(board)
            print()
            checkwin(board)
        else:
            print("Game is a draw. ")
            sys.exit()
    else: #if the number is not 1, the bot will go first
        print('''
Welcome to the Tic Tac Toe game! You will be playing against a robot. Randomly, the starter has been assigned as BOT.''')
        time.sleep(1)
        while moves <= 8:
            moves += 1
            if moves <= 2:
                first_two_botmove(board)
                print("\n THE BOT WILL MOVE: ")
                board_print(board)
                print('''
    Now you will move.''')
                moveuser(board)
                board_print(board)
            elif moves == 3 and str(board[1][1]) != "X":
                board[1][1] = "O"
                print("\n THE BOT WILL MOVE: ")
                board_print(board)
                checkwin(board)
                print('''
Now you will move.''')
                moveuser(board)
                board_print(board)
                checkwin(board)
            else:
                rowbot, colbot = botmove(board)
                board[rowbot][colbot] = "O"
                print("\n THE BOT WILL MOVE: ")
                board_print(board)
                checkwin(board)
                print('''
    Now you will move.''')
                moveuser(board)
                board_print(board)
                checkwin(board)
        else:
            print("Game is a draw. ")
            sys.exit()


if __name__ == "__main__":
    main()
