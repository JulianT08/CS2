'''
Name: toub_julian_hangman


Log: 1
'''
import random

def show_diagram(tries, new_list, guessed, word):
    '''
    Prints the hangman structure depending on how many tries left. Prints the guessed list. 

    Args:
        tries(int): How many tries left.
        new_list(str): A list of blanks with any correctly guessed letters filled out. 
        guessed(list): A list of the guessed letters.
        word(str): The word. 
    
    Returns:
        none 

    Raises:
        none 
    '''
    if tries == 7:
        diagram = f'''

    The word is {new_list}
    You have {tries} tries left.                            You have guessed: {guessed}
        
            ________
            |       |
            |       |
                    |
                    |
                    |
                    |
                    |
                    |
        =====================

'''
        print(diagram)
    elif tries == 6:
        diagram = f'''

    The word is {new_list}
    You have {tries} tries left.                            You have guessed: {guessed}
     
            ________
            |       |
            |       |
            O       |
                    |
                    |
                    |
                    |
                    |
        =====================
    
'''
        print(diagram)
    elif tries == 5:
        diagram = f'''

    The word is {new_list}
    You have {tries} tries left.                            You have guessed: {guessed}
    
            ________
            |       |
            |       |
            O       |
            |       |
                    |
                    |
                    |
                    |
        =====================

'''       
        print(diagram)

    elif tries == 4:
        diagram = f'''

    The word is {new_list}
    You have {tries} tries left.                            You have guessed: {guessed}
    
            ________
            |       |
            |       |
            O       |
            |       |
            |       |
                    |
                    |
                    |
        =====================

'''       
        print(diagram)
    elif tries == 3:
        diagram = f'''

    The word is {new_list}
    You have {tries} tries left.                            You have guessed: {guessed}
    
            ________
            |       |
            |       |
            O       |
          \ |       |
            |       |
                    |
                    |
                    |
        =====================

'''        
        print(diagram)
    elif tries == 2:
        diagram = f'''

    The word is {new_list}
    You have {tries} tries left.                            You have guessed: {guessed}
    
            ________
            |       |
            |       |
            O       |
          \ | /     |
            |       |
                    |
                    |
                    |
        =====================

'''       
        print(diagram)
    elif tries == 1:
        diagram = f'''

    The word is {new_list}
    You have {tries} tries left.                            You have guessed: {guessed}
    
            ________
            |       |
            |       |
            O       |
          \ | /     |
            |       |
           /        |
                    |
                    |
        =====================

'''          
        print(diagram)
    elif tries == 0:
        diagram = f'''

    The word is {new_list}
    You have {tries} tries left.                            You have guessed: {guessed}
      
             ________
            |       |
            |       |
            0       |
          \ | /     |
            |       |
           / \      |
                    |
                    |
        =====================

'''       
        print(diagram)
def get_guess(guess, guessed, guessed_word, word, won, lost, user_score, bot_score):
    '''
    Retrieves the guess from the user, verifies that it fits the parameters and allows them to guess the word. 

    Args:
        guess(str): The user's guess.
        guessed(list): The list of guessed words.
        guessed_word(str): The user's guess for the word. 
        word(str): The word. 
        won(bool): Whether or not the user has won yet. 
        lost(bool): Whether or not the user has lost yet. 
        user_score(int): The user's score against the bot. 
        bot_score(int): The bot's score against the user. 
    
    Returns:
        guess(str): The user's guess.
        guessed(list): The list of guessed words.


    Raises:
        none 
    '''
    while True:
        guess = str.lower(input("Enter your guess or type 'word' to guess the word: "))
        if guess.isalpha() and len(guess) == 1:
            guessed.append(guess)
            while "" in guessed:
                guessed.remove("")
            return guess, guessed
        elif guess == "word":
            guess_word(guessed_word, word, won, lost, user_score, bot_score)
            return guess, guessed
            
        else:
            print("Guess must be a single letter without any spaces. (e.g. 'a' or 'b' or 'c') ")
def blanks(word):
    '''
    Makes a list of underscores the length of the word. 

    Args:
        word(str): The word.
    
    Returns:
        word_list(str): The underscores the same length as the word (ex. _ _ _ ).  

    Raises:
        none
    '''
    word_list = str("_")*len(word)
    return word_list


def check_guess(guess, word, new_list, tries):
    '''
    Checks if the guessed letter is in the word and adjusts the blank list and the tries. 

    Args:
        guess(str): The user's guess.
        word(str): The word.     
        new_list(str): A list of blanks with any correctly guessed letters filled out. 
        tries(int): How many tries left.

    Returns:
        (" ".join(new_list)): The new_list function converted into a string with the correct format. 
        tries(int): How many tries left.
    Raises:
        none 
    '''
    split_word = list(word)
    for i in range(len(split_word)):
        if split_word[i] == guess:
            new_list = list(new_list)
            while ' ' in new_list:
                new_list.remove(' ')
            new_list[i] = guess 
        elif guess not in split_word:
            new_list = list(new_list)
            while ' ' in new_list:
                new_list.remove(' ')
            tries -= 1/len(word)
    return (" ".join(new_list)), int(tries)

def checkwin(tries, new_list, user_score, bot_score, won, lost, word):
    '''
    Checks if the user has won or lost. 

    Args:
        tries(int): How many tries left.
        new_list(str): A list of blanks with any correctly guessed letters filled out. 
        user_score(int): The user's score against the bot. 
        bot_score(int): The bot's score against the user. 
        won(bool): Whether or not the user has won yet. 
        lost(bool): Whether or not the user has lost yet. 
        word(str): The word.     

    Returns:
        user_score(int): The user's score against the bot. 
        bot_score(int): The bot's score against the user. 
        won(bool): Whether or not the user has won yet. 
        lost(bool): Whether or not the user has lost yet. 

    Raises:
        none 
    '''
    if tries > 0 and "_" not in new_list:
        print("Game is over, you win!")
        user_score += 1
        won = True
        lost = False
        return user_score, bot_score, won, lost
    elif tries == 0:
        print(f"Game is over you lose. The word was '{word}'")
        bot_score += 1
        won = True
        lost = False
        return user_score, bot_score, won, lost
    return user_score, bot_score, won, lost  

def guess_word(guessed_word, word, won, lost, user_score, bot_score):
    '''
    Gets the guess for the full word. 

    Args:
        guessed_word(str): The user's guess for the word. 
        word(str): The word.     
        won(bool): Whether or not the user has won yet. 
        lost(bool): Whether or not the user has lost yet. 
        user_score(int): The user's score against the bot. 
        bot_score(int): The bot's score against the user. 
    
    Returns:
        user_score(int): The user's score against the bot. 
        bot_score(int): The bot's score against the user. 
        won(bool): Whether or not the user has won yet. 
        lost(bool): Whether or not the user has lost yet. 

    Raises:
        none 
    '''
    guessed_word = str.lower(input("Guess the word: "))
    if guessed_word == word:
        print("Game is over, you win!")
        user_score += 1
        won = True
        lost = False
        return user_score, won, lost
    else:
        print(f"Game is over you lose. The word was '{word}'")
        bot_score += 1
        won = False
        lost = True
        return bot_score, won, lost

def display_scoreboard(user_score, bot_score):
    '''
    Prints the overall User vs Bot scoreboard. 

    Args:
        user_score(int): The user's score against the bot. 
        bot_score(int): The bot's score against the user. 
    
    Returns:
        none

    Raises:
        none 
    '''
    print(f'''
+---------------------+
|     SCOREBOARD      |
+---------------------+
| USER     |  BOT     |
+---------------------+
|   {user_score}      |  {bot_score}       |
+---------------------+
''')

def main():
    user_score = 0 # starts the game with 0 points for the user
    bot_score = 0 # starts the game with 0 points for the bot
    with open('1-1000.txt', 'r') as f:
        words = f.read().split('\n') # reads in the text file for the most common 1000 words and sets "words" = to the words in the file
    while True:
        play = str.lower(input("Would you like to play? (yes / no): ")) # asks the user if they want to play
        won = False # sets the status of "won" to false
        lost = False # sets the status of "lost" to false
        if 'y' in play:
            tries = 7  # the user gets 7 initial attempts
            word = str.lower(random.choice(words)) # picks a random word from the list "words" sets that = to "word"
            new_list = list(blanks(word)) # creates the blanks list
            guess = "" 
            guessed = [""]
            guessed_word = ""
            show_diagram(tries, new_list, guessed, word) # shows the hangman picture

            while tries >= 0 and won == False and lost == False: # while the user still has tries and they havent won or lost:
                guess, guessed = get_guess(guess, guessed, guessed_word, word, won, lost, user_score, bot_score) 
                checkwin(tries, new_list, user_score, bot_score, won, lost, word) # checks for a win or loss
                if won == False and lost == False: # if the user hasn't won or lost:
                    new_list, tries = check_guess(guess, word, new_list, tries)
                    show_diagram(tries, new_list, guessed, word) # shows the hangman picture
                    user_score, bot_score, won, lost = checkwin(tries, new_list, user_score, bot_score, won, lost, word)
                    display_scoreboard(user_score, bot_score) # show the scoreboard


        elif 'n' in play:
            print("Ok, bye!") # if the user doesn't want to play, say bye
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.") # if the user didn't input a 'y' or 'n' give them an error

if __name__ == "__main__":
    main()
