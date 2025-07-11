'''
toub_julian_battleship.py

Description: This code is a take on the popular boardgame battleship. The user will play against
the computer that randomly generates 5 spots for its ships and randomly generates moves. The user is told
to place their 5 ships and then make moves to hit their opponents' ships. The user has the option to get 
hints as to where the ships are.

Features: 
    Hint feature: allows the user to get a hint that partially reveals the location of a ship. 
    Time pauses: Pauses the program to allow for the user to see previous moves. 
    Win Checks: Checks for any wins by checking to see if both players still have unguessed ships. 

Log: 1.0

Bugs: Shows the user that their ship hasn't been placed in the case of an error but doesn't state why. 

Tested By: Owen Chickering and Penelope Shepherd 
'''



import random
import time
import sys


bot_turns = 0 #Sets the bot turns equal to 0. 
# This is the table for the positions of the bot.
# When showing the board, each cell will reference a position in this list
bot_positions = [
    '1','2','3','4','5',
    '6','7','8','9','10',
    '11','12','13','14','15',
    '16','17','18','19','20',
    '21','22','23','24','25']

# This is the table for the positions of the user.
# When showing the board, each cell will reference a position in this list
user_positions = [
    '1','2','3','4','5',
    '6','7','8','9','10',
    '11','12','13','14','15',
    '16','17','18','19','20',
    '21','22','23','24','25']

# The bot will choose a random number from this list and use it as the index for their move
bot_choices = list(range(25))
user_guesses = []
# The user will pick an item from this list for their move
user_choices = [
    '1','2','3','4','5',
    '6','7','8','9','10',
    '11','12','13','14','15',
    '16','17','18','19','20',
    '21','22','23','24','25']
bot_ships = []
def update_bot_board():
    '''
    Updates the bot's board so that when it prints the board, it is refrencing the up-to-date variables. 

    Args:
        none
    
    Returns:
        bot_board(str): The bot's board.  

    Raises:
        none
    '''
    bot_board = f'''
BOT BOARD:
________________________________
   {bot_positions[0]}  |  {bot_positions[1]}  |  {bot_positions[2]}  |  {bot_positions[3]}  |  {bot_positions[4]}  
________________________________
   {bot_positions[5]}  |  {bot_positions[6]}  |  {bot_positions[7]}  |  {bot_positions[8]}  |  {bot_positions[9]} 
________________________________
   {bot_positions[10]} |  {bot_positions[11]} |  {bot_positions[12]} |  {bot_positions[13]} |  {bot_positions[14]} 
________________________________
   {bot_positions[15]} |  {bot_positions[16]} |  {bot_positions[17]} |  {bot_positions[18]} |  {bot_positions[19]} 
________________________________
   {bot_positions[20]} |  {bot_positions[21]} |  {bot_positions[22]} |  {bot_positions[23]} |  {bot_positions[24]} 
________________________________
'''
    return bot_board
def update_user_board():
    '''
    Updates the user's board so that when it prints the board, it is refrencing the up-to-date variables. 

    Args:
        none
    
    Returns:
        user_board(str): The user's board.  

    Raises:
        none
    '''
    user_board = f'''
USER BOARD:
________________________________
   {user_positions[0]}  |  {user_positions[1]}  |  {user_positions[2]}  |  {user_positions[3]}  |  {user_positions[4]}  
________________________________
   {user_positions[5]}  |  {user_positions[6]}  |  {user_positions[7]}  |  {user_positions[8]}  |  {user_positions[9]} 
________________________________
   {user_positions[10]} |  {user_positions[11]} |  {user_positions[12]} |  {user_positions[13]} |  {user_positions[14]} 
________________________________
   {user_positions[15]} |  {user_positions[16]} |  {user_positions[17]} |  {user_positions[18]} |  {user_positions[19]} 
________________________________
   {user_positions[20]} |  {user_positions[21]} |  {user_positions[22]} |  {user_positions[23]} |  {user_positions[24]} 
________________________________
'''
    return user_board

def show_bot_board():
    '''
    Prints the bot's board. 

    Args:
        none
    
    Returns:
        none 

    Raises:
        none
    '''
    bot_board = update_bot_board()
    print(bot_board)
def show_user_board():
    '''
    Prints the user's board. 

    Args:
        none
    
    Returns:
        none 

    Raises:
        none
    '''
    user_board = update_user_board()
    print(user_board)

def bot_setup():
    '''
    Sets up the bot's board. Creates a list of indices from 0 - 24. Then, picks a random number and removes it from
    the list and applies the index to the list, bot_positions. Finally, a ship is picked using the following logic
    ship = possible_positions[random index].

    Args:
        none
    
    Returns:
        bot_ships(list): The list of bot ship positions. 

    Raises:
        none
    ''' 
    choices = list(range(0, 25))
    for i in range(5):
        index = random.choice(choices)
        choices.remove(index)
        bot_ships.append(bot_positions[index])
    return bot_ships
def user_setup():
    '''
    Allows the user to set up its board. The user enters a number for where they want their placed.
    It then confirms whether the ship was placed or not based off if the input fits the requirements. 

    Args:
        none
    
    Returns:
        user_positions(list): The list of user ship positions. 

    Raises:
        none
    ''' 
    for choice in range(5):
        while True:
            user_choice = input("Enter the location for your ship. Must be between 1 and 25. ")
            if user_choice in user_positions:
                for i in user_positions:
                    if user_choice == i:
                        index = user_positions.index(i)
                        user_positions[index] = "🚢"
                        print(f"Ship placed at {user_choice}")
                break
    return user_positions

def pick_first():
    '''
    Picks who goes first. Simple heads or tails game.  

    Args:
        none
    
    Returns:
        True or False(bool): True if the user wins, false if not.

    Raises:
        none
    ''' 
    heads = "heads"
    tails = "tails"
    options = [heads, tails]
    answer = str.lower(random.choice([heads, tails]))
    while True:
        heads_or_tails = str.lower(input("Now we will pick who goes first.... Heads or Tails? "))
        if heads_or_tails in options:
            if heads_or_tails == answer:
                return True
            else:
                return False

def bot_pick():
    '''
    Makes a random move for the bot using a list that is constantly updated with the viable moves. 
    Shows whether the bot hit or missed using emojis. 

    Args:
        none
    
    Returns:
        bot_positions(list[str]): The list of bot ship positions. 
        bot_choices(list[int]): The list of possible choices for the bot.
        bot_turns(int): The number of moves that have been done by the bot. 

    Raises:
        none
    ''' 
    global bot_turns
    index = random.choice(bot_choices[:len(user_positions)])
    bot_choices.remove(index)
    bot_turns += 1
    print(f"Bot picked: {user_positions[index]}")
    if user_positions[index] == "🚢":
        user_positions[index] = "💥"
    else:
        user_positions[index] = "💦"
    return bot_positions, bot_choices, bot_turns
def user_pick():
    '''
    Lets the user make a move. Shows whether the move was a hit or miss using emojis. 
    Updates the bot_positions to reflect the users move.  

    Args:
        none
    
    Returns:
        bot_positions(list[str]): The list of bot ship positions. 
        user_choices(list[str]): The list of possible user moves. 

    Raises:
        none
    ''' 
    while True:
        choice = input("Enter the spot of your move.  OR TYPE 'H' FOR A HINT.  ").lower()
        if choice.lower() == "h":
            give_hint()

        elif choice in user_choices:
            user_guesses.append(choice)
            if choice in bot_ships:
                if choice in user_choices:
                    bot_positions[user_choices.index(choice)] = "💥"
                    bot_ships.remove(choice)
                choice = input("Well done hitting the ship, GO AGAIN. Enter the coordinates of your move. ").lower()
                if choice in user_choices:
                    user_guesses.append(choice)
                    if choice in bot_ships:
                        bot_positions[user_choices.index(choice)] = "💥"
                        bot_ships.remove(choice)
                    else:
                        bot_positions[user_choices.index(choice)] = "💦"

            else:
                bot_positions[user_choices.index(choice)] = "💦"

                return bot_positions, user_choices
            break
def give_hint():
    '''
    Gives the user a hint as to the row of an unguessed ship.  
    Prints the row. 
    
    Args:
        none
    
    Returns:
        none 
    
    Raises:
        none
    '''   
    random_ship = random.choice(bot_ships)
    ship_index = bot_positions.index(random_ship)
    row_number = (ship_index // 5) + 1  # Calculate row number (1-based index)
    print(f"Here is a hint, one of the ships' location is in row {row_number}")

def check_user_win():
    '''
    Checks if the user has won the game by eliminating all of the bot's ships.  

    Args:
        none
    
    Returns:
        True or False(bool): True if the user wins, false if not.

    Raises:
        none
    ''' 
    if not bot_ships:
        return True
    else:
        return False
def check_bot_win():
    '''
    Checks if the bot has won the game by eliminating all of the user's ships.  

    Args:
        none
    
    Returns:
        True or False(bool): True if the user wins, false if not.

    Raises:
        none
    ''' 
    if "🚢" not in user_positions:
        return True
    else:
        return False

def user_out_of_guesses():
    '''
    Checks if the user is out of guesses.  

    Args:
        none
    
    Returns:
        True or False(bool): True if the user is out of guesses, false if not.

    Raises:
        none
    ''' 
    if len(user_guesses) >= 10:
        return True
    else:
        return False
def bot_out_of_guesses():
    '''
    Checks if the bot is out of guesses.  

    Args:
        none
    
    Returns:
        True or False(bool): True if the bot is out of guesses, false if not.

    Raises:
        none
    ''' 
    if bot_turns >= 10:
        return True
    else:
        return False
def main():
    #Setting up the BOT's board
    bot_setup()
    show_bot_board()
    #Setting up the USER's board
    show_user_board()
    user_setup()
    show_user_board()
    #Pick who goes first and carry out the following scenarios based on the first player
    if pick_first():
        print("User goes first! ")
        while check_user_win() == False and check_bot_win() == False:
            if user_out_of_guesses(): #If the user is out of guesses, they lose.
                print('''
                      BOOOO, you lose. Out of guesses :(''')
                sys.exit()
            elif bot_out_of_guesses(): #If the bot is out of guesses, it loses. 
                print('''
                      Well done! You win. Bot is out of guesses :)''')
                sys.exit()
            show_bot_board()     
            user_pick()
            show_bot_board()
            time.sleep(2)
            bot_pick()
            show_user_board()
            time.sleep(2)
            if check_user_win():
                print('''
                      Well done! You win.''')
                sys.exit()
            elif check_bot_win():
                print('''
                      BOOOO, you lose. ''')
                sys.exit()

    else:
        print("Bot goes first :( ")
        while check_user_win() == False and check_bot_win() == False:
            if user_out_of_guesses(): #If the user is out of guesses, they lose.
                print('''
                      BOOOO, you lose. Out of guesses :(''')
                sys.exit()
            elif bot_out_of_guesses(): #If the bot is out of guesses, it loses.
                print('''
                      Well done! You win. Bot is out of guesses :)''')
                sys.exit()
            bot_pick()
            show_user_board()
            time.sleep(3)
            user_pick()
            show_bot_board()
        if check_user_win():
            print("Well done! You win.")
            sys.exit()
        elif check_bot_win():
            print("BOOOO, you lose. ")
            sys.exit()

if __name__ == "__main__":
    main()