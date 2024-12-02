'''
Name: toub_julian_tictactoe.py
Description: This code allows the user to play Tic Tac Toe against a robot. The robot will play 
statistically smart moves at the beginning. After that, it randomly reacts to the user's moves.

Bugs: none found

Features: bot plays intelligent first 2-3 moves.  

Sources: https://www.geeksforgeeks.org/python-using-2d-arrays-lists-the-right-way/

Log: 1
'''

import random
import sys
import time
def board_print(board):
    """
    Prints the board by iterating through the length of it (3x3).

    Args:
        board(list): A list of the 3 rows.

    Returns:
        Prints the board item by item.

    Raises:
        none
    """
    for row in range(len(board)):
        for col in range(len(board[row])):
            print(board[row][col], end=' ')
        print()

def moveuser(board):
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
    if board_full(board) == True:
        print("The game is a draw, no more places to move. ")
        sys.exit()
    while True:
        userchoice = input("Move: ")
        if userchoice.isdigit() and int(userchoice) <= 9:
            if int(userchoice) == 1 and str(board[0][0]) != "X" and str(board[0][0]) != "O":
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
                print("Spot is taken. ")
        else:
            print('''
Make sure that you are not attempting to place your move on top of opponents move or your own move. 
AND that your move is a number 1-9. \n''')

def first_two_botmove(board):
    """
    Generates a random corner for the bot to move to. The valid options are any corners spots.

    Args:
        board(list): A list of the 3 rows.

    Returns:
        move(any): The coordinates for the bot's move.

    Raises:
        none
    """
    rows = random.choice([0, 2])
    cols = random.choice([0, 2])
    move = board[rows][cols]    
    while str(board[rows][cols]) == "X" or str(board[rows][cols]) == "O":
        rows = random.choice([0, 2])
        cols = random.choice([0, 2])
        move = board[rows][cols]
    board[rows][cols] = "O"  
    return move

def botmove(board):
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
    if board_full(board) == True:
        print("The game is a draw, no more places to move. ")
        sys.exit()
    while True:
        rowbot = random.randint(0,2)
        colbot = random.randint(0,2)
        while str(board[rowbot][colbot]) == "X" or str(board[rowbot][colbot]) == "O":
            rowbot = random.randint(0,2)
            colbot = random.randint(0,2)
        return rowbot, colbot
def checkwin(board, player):
    """
    Checks if either the user or the bot has made a winning combination. 

    Args:
        board(list): A list of the 3 rows.
        player(string): Either "X" or "O"

    Returns:
        none

    Raises:
        none
    """
    if board[0][0]== player and board[0][1]== player and board[0][2]== player:
        print(f"GAME HAS BEEN WON BY {player} \n")
        sys.exit()
    elif board[1][0]== player and board[1][1]== player and board[1][2]== player:
        print(f"GAME HAS BEEN WON BY {player} \n")
        sys.exit()
    elif board[2][0]== player and board[2][1]== player and board[2][2]== player:
        print(f"GAME HAS BEEN WON BY {player} \n")
        sys.exit()
    elif board[0][0]== player and board[1][1]== player and board[2][2]== player:
        print(f"GAME HAS BEEN WON BY {player} \n")
        sys.exit()
    elif board[2][0]== player and board[1][1]== player and board[0][2]== player:
        print(f"GAME HAS BEEN WON BY {player} \n")
        sys.exit()
    elif board[0][0]== player and board[1][0]==player and board[2][0]== player:
        print(f"GAME HAS BEEN WON BY {player} \n")
        sys.exit()
    elif board[0][1]== player and board[1][1]== player and board[2][1]==player:
        print(f"GAME HAS BEEN WON BY {player} \n")
        sys.exit()
    elif board[0][2]== player and board[1][2]== player and board[2][2]== player:
        print(f"GAME HAS BEEN WON BY {player} \n")
        sys.exit()

def board_full(board):
    """
    Checks if the board is completely filled.

    Args:
        board(list): A list of the 3 rows.

    Returns:
        True or false.

    Raises:
        none
    """
    for row in board:
        for spot in row:
            if spot not in ["X", "O"]:
                return False
    return True

def main():
    
    board = [[1,2,3],                       #defining the board as a 3 x 3 box, numbered 1-9. 
         [4,5,6],
         [7,8,9]]

    moves = 0                               #sets moves to 0
    print('''
User = X
Bot = O''')                                 #prints the corresponding letter to the player. User = X, Bot = O
    random_num = random.randint(1,2)        #generates a random number 1-2
    
    if random_num == 1:                     #if the random number is 1, the user will go first
        while moves <= 8:     
            if moves == 0:                  #if the moves are equal to 0, the board will print     
                board_print(board)          #print the board
            moves += 1                
            moveuser(board)                 #user move
            board_print(board)              #print the board
            checkwin(board, "X")
            checkwin(board, "O")
            if moves <= 2:
                moves += 1
                first_two_botmove(board)    #function to go to a corner spot
                print("\n NOW THE BOT WILL MOVE: ")
                board_print(board)          #print the board
            elif moves == 3 and str(board[1][1]) != "X":    #if it is the 3rd move and the middle spot is open, the bot will take that spot
                moves += 1
                board[1][1] = "O"           #places an "O" in the middle spot
                print("\n NOW THE BOT WILL MOVE: ")
                board_print(board)          #print the board
                checkwin(board, "X")        #checks if the user has won
                checkwin(board, "O")        #checks if the bot has won
                print('''
Now you will move.''')
                moves += 1
                moveuser(board)             #user move
                board_print(board)          #print the board
                checkwin(board, "X")        #checks if the user has won
                checkwin(board, "O")        #checks if the bot has won
                moves += 1
                rowbot, colbot = botmove(board) #bot move
                board[rowbot][colbot] = "O" #places an "O" on the generated spot
                print("\n NOW THE BOT WILL MOVE: ")
                time.sleep(1)               #one second pause
                board_print(board)          #print the board
                print()
                checkwin(board, "X")        #checks if the user has won
                checkwin(board, "O")        #checks if the bot has won

            
            else:                           #if the moves are greater than 3:
                checkwin(board, "X")        #checks if the user has won
                checkwin(board, "O")        #checks if the bot has won
                moves += 1
                rowbot, colbot = botmove(board) #bot move
                board[rowbot][colbot] = "O" #places an "O" on the generated spot
                print("\n NOW THE BOT WILL MOVE: ")
                time.sleep(1)               #one second pause
                board_print(board)          #print the board
                print()
                checkwin(board, "X")        #checks if the user has won
                checkwin(board, "O")        #checks if the bot has won

        else:                               #if there have been 9 moves and nobody has won, the game is a draw
            print("Game is a draw. ")
            sys.exit()
    else:                                   #if the number is not 1, the bot will go first
        print('''
Welcome to the Tic Tac Toe game! You will be playing against a robot. Randomly, the starter has been assigned as BOT.''')
        time.sleep(1)
        while moves <= 8:
            if moves <= 2:
                moves += 1
                first_two_botmove(board)    #function to go to a corner spot
                print("\n THE BOT WILL MOVE: ")
                board_print(board)          #prints the board
                print('''
    Now you will move.''')
                moves += 1
                moveuser(board)             #user move
                board_print(board)
            elif moves == 4 and str(board[1][1]) != "X":    #if it is the 3rd move and the middle spot is open, the bot will take that spot
                moves += 1
                board[1][1] = "O"           #place an "O" in the middle
                print("\n THE BOT WILL MOVE: ")
                board_print(board)          #prints the board
                checkwin(board, "X")        #checks if the user has won
                checkwin(board, "O")        #checks if the bot has won
                print('''
Now you will move.''')
                moves += 1        
                moveuser(board)
                board_print(board)
                checkwin(board, "X")        #checks if the user has won
                checkwin(board, "O")        #checks if the bot has won

            else:                           #if the moves are greater than 3:
                moves += 1
                rowbot, colbot = botmove(board) #bot move
                board[rowbot][colbot] = "O"     #place an "O" on the generated spot
                print("\n THE BOT WILL MOVE: ")
                board_print(board)
                checkwin(board, "X")        #checks if the user has won
                checkwin(board, "O")        #checks if the bot has won
                print('''
    Now you will move.''')
                moves += 1
                moveuser(board)
                board_print(board)
                checkwin(board, "X")     #checks if the bot has won
                checkwin(board, "O")      #checks if the bot has won

        else:                               #if there have been 9 moves and nobody has won, the game is a draw
            print("Game is a draw. ")
            sys.exit()


if __name__ == "__main__":
    main()
