'''
Name: toub_julian_hangman


Log: 1
'''
import random
import tkinter as tk

def show_diagram(tries, new_list, guessed):
    if tries == 6:
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
    elif tries == 5:
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
def get_guess(guess, guessed):
    while True:
        guess = str.lower(input("Enter your guess: "))
        if guess.isalpha() and len(guess) == 1:
            guessed.append(guess)
            while "" in guessed:
                guessed.remove("")
            return guess, guessed
        else:
            print("Guess must be a single letter without any spaces. (e.g. 'a' or 'b' or 'c') ")
def blanks(word):
    word_list = str("_")*len(word)
    return word_list


def check_guess(guess, word, new_list, tries):
    split_word = list(word)
    for i in range(len(split_word)):
        if split_word[i] == guess:
            new_list = list(new_list)
            while ' ' in new_list:
                new_list.remove(' ')
            new_list[i] = guess #split the word!
        elif guess not in split_word:
            new_list = list(new_list)
            while ' ' in new_list:
                new_list.remove(' ')
            tries -= 1/len(word)
    return (" ".join(new_list)), int(tries)

def checkwin(tries, new_list, user_score, bot_score, won, lost):
    if tries > 0 and "_" not in new_list:
        print("Game is over, you win!")
        user_score += 1
        won = True
        lost = False
        return user_score, bot_score, won, lost
    elif tries == 0:
        print("Game is over you lose. ")
        bot_score += 1
        won = True
        lost = False
        return user_score, bot_score, won, lost
    return user_score, bot_score, won, lost  

def guess_word(guessed_word, word, won, lost, user_score, bot_score):
    guessed_word = str.lower(input("Guess the word: "))
    if guessed_word == word:
        print("Game is over, you win!")
        user_score += 1
        won = True
        lost = False
        return user_score, won, lost
    else:
        print("Game is over you lose. ")
        bot_score += 1
        won = True
        lost = False
        return bot_score, won, lost

def display_scoreboard(user_score, bot_score):
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
    user_score = 0
    bot_score = 0
    with open('1-1000.txt', 'r') as f:
        words = f.read().split('\n')
    while True:
        play = str.lower(input("Would you like to play? (yes / no): "))
        won = False
        lost = False
        if 'y' in play:
            tries = 6  # the user gets 6 initial attempts
            word = str.lower(random.choice(words))
            new_list = list(blanks(word))
            guess = ""
            guessed = [""]
            guessed_word = ""

            while tries >= 0 and won == False:
                guess, guessed = get_guess(guess, guessed)
                new_list, tries = check_guess(guess, word, new_list, tries)
                show_diagram(tries, new_list, guessed)
                user_score, bot_score, won, lost = checkwin(tries, new_list, user_score, bot_score, won, lost)
                display_scoreboard(user_score, bot_score)
                want_to_guess = str.lower(input("Would you like to guess the word? You will lose if you guess wrong. "))
                if "y" in want_to_guess:
                    guess_word(guessed_word, word, won, lost, user_score, bot_score)

        elif 'n' in play:
            print("Thanks for playing!")
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

if __name__ == "__main__":
    main()

'''
def hangman():
    tries = 6  # the user gets 6 initial attempts
    word = str.lower("Dog")
    new_list = list(blanks(word))
    guess = ""
    guessed = [""]

    while tries >= 0:
        guess, guessed = get_guess(guess, guessed)
        new_list, tries = check_guess(guess, word, new_list, tries)
        show_diagram(tries, new_list, guessed)
        checkwin(tries, new_list)
def start_game():
    global game_running
    if not game_running:
        game_running = True
        start_button.pack_forget()  # Hide the button after it's clicked
        hangman()
        game_running = False

if __name__ == "__main__":
    # Create a tkinter window
    root = tk.Tk()
    root.title("Hangman Game")
    root.geometry("300x150")

    game_running = False  # Global flag to track if the game is already running

    # Create a button to start the game
    start_button = tk.Button(root, text="Start Hangman Game", command=start_game, font=("Arial", 14))
    start_button.pack(pady=50)

    # Run the tkinter main loop
    root.mainloop()
    '''


