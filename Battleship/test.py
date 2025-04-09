import random
import time
#This is the table for the positions of the bot. 
#When showing the board, each cell will reference a position in this list
bot_positions = [
    'a1','a2','a3','a4','a5',
    'b1','b2','b3','b4','b5',
    'c1','c2','c3','c4','c5',
    'd1','d2','d3','d4','d5',
    'e1','e2','e3','e4','e5']

#This is the table for the positions of the user. 
#When showing the board, each cell will reference a position in this list
user_positions = [
    'a1','a2','a3','a4','a5',
    'b1','b2','b3','b4','b5',
    'c1','c2','c3','c4','c5',
    'd1','d2','d3','d4','d5',
    'e1','e2','e3','e4','e5']

#The bot will choose a random number from this list and use it as the index for their move
bot_choices = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]

#The user will pick an item from this list for their move
user_choices = [
    'a1','a2','a3','a4','a5',
    'b1','b2','b3','b4','b5',
    'c1','c2','c3','c4','c5',
    'd1','d2','d3','d4','d5',
    'e1','e2','e3','e4','e5']
bot_ships = []
def update_bot_board():
    bot_board = f'''
BOT BOARD:
 ________________________
| {bot_positions[0]} || {bot_positions[1]} || {bot_positions[2]} || {bot_positions[3]} || {bot_positions[4]} |
 ________________________
| {bot_positions[5]} || {bot_positions[6]} || {bot_positions[7]} || {bot_positions[8]} || {bot_positions[9]} | 
 ________________________
| {bot_positions[10]} || {bot_positions[11]} || {bot_positions[12]} || {bot_positions[13]} || {bot_positions[14]} |
 ________________________
| {bot_positions[15]} || {bot_positions[16]} || {bot_positions[17]} || {bot_positions[18]} || {bot_positions[19]} |
 ________________________
| {bot_positions[20]} || {bot_positions[21]} || {bot_positions[22]} || {bot_positions[23]} || {bot_positions[24]} |
 ________________________
 '''
    return bot_board
def update_user_board():
    user_board = f'''
USER BOARD:
 ________________________
| {user_positions[0]} || {user_positions[1]} || {user_positions[2]} || {user_positions[3]} || {user_positions[4]} |
 ________________________
| {user_positions[5]} || {user_positions[6]} || {user_positions[7]} || {user_positions[8]} || {user_positions[9]} | 
 ________________________
| {user_positions[10]} || {user_positions[11]} || {user_positions[12]} || {user_positions[13]} || {user_positions[14]} |
 ________________________
| {user_positions[15]} || {user_positions[16]} || {user_positions[17]} || {user_positions[18]} || {user_positions[19]} |
 ________________________
| {user_positions[20]} || {user_positions[21]} || {user_positions[22]} || {user_positions[23]} || {user_positions[24]} |
 ________________________
 '''
    return user_board

def show_bot_board():
    bot_board = update_bot_board()
    print(bot_board)
def show_user_board():
    user_board = update_user_board()
    print(user_board)

def bot_setup():
    for i in range(5):
        choices = list(range(0, 25))
        index = random.choice(choices)
        choices.remove(index)
        bot_ships.append(bot_positions[index])
    return bot_ships
def user_setup():
    for choice in range(5):
        user_choice = str.lower(input("Enter the coordinates for your ship. "))
        if user_choice in user_positions:
            for i in user_positions:
                if user_choice == i:
                    index = user_positions.index(i)
                    user_positions[index] = "S"
    return user_positions

def pick_first():
    heads = "heads"
    tails = "tails"
    answer = str.lower(random.choice([heads, tails]))
    heads_or_tails = str.lower(input("Now we will pick who goes first.... Heads or Tails? "))
    if heads_or_tails == answer:
        return True
    else:
        return False

def bot_pick():
    index = random.choice(bot_choices)
    bot_choices.remove(index)
    print(f"Bot picked: {user_positions[index]}")
    if user_positions[index] == "S":
        print("HIT")       
        user_positions[index] = "H"
    return bot_positions, bot_choices
def user_pick():
    while True:
        choice = input("Enter the coordinates of your move.  ").lower()
        if choice in user_choices:
            if choice in bot_ships:
                print("HIT")
                bot_positions[user_choices.index(choice)] = "H"
                bot_ships.remove(choice)
                return bot_positions, user_choices
            break

def check_user_win():
    if not bot_ships:
        return True
    else:
        return False
def check_bot_win():
    if "S" not in user_positions:
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
            show_bot_board()
            user_pick()
            time.sleep(2)
            bot_pick()
            show_user_board
            time.sleep(3)
        if check_user_win():
            print("Well done! You win.")
        elif check_bot_win():
            print("BOOOO, you lose. ")

    else:
        print("Bot goes first :( ")
        while check_user_win() == False and check_bot_win() == False:
            bot_pick()
            show_user_board()
            time.sleep(3)
            show_bot_board()
            user_pick()
        if check_user_win():
            print("Well done! You win.")
        elif check_bot_win():
            print("BOOOO, you lose. ")

if __name__ == "__main__":
    main()