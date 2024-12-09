'''
Name: toub_julian_hangman


Log: 1
'''
import sys
def show_diagram(tries, new_list):
    if tries == 6:
        diagram = f'''

    The word is {new_list}
    You have {tries} tries left. 
        
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
    You have {tries} tries left. 
     
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
    You have {tries} tries left. 
    
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
    You have {tries} tries left. 
    
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
    You have {tries} tries left. 
    
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
    You have {tries} tries left. 
    
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
    You have {tries} tries left. 
      
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
def get_guess(guess):
    while True:
        guess = str.lower(input("Enter your guess: "))
        if guess.isalpha():
            return guess
        else:
            print("Guess must be a letter. (e.g. a b c ) ")
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
            print(new_list)
            new_list[i] = guess #split the word!
        elif guess not in split_word:
            tries -= 1/len(word)
    return (" ".join(new_list)), int(tries)
def checkwin(tries, new_list):
    if tries > 0 and "_" not in new_list:
        print("Game is over, you win!")
        sys.exit()
    elif tries == 0:
        print("Game is over you lose. ")
        sys.exit()

def main():
    tries = 6 #the user gets 6 initial attempts
    word = str.lower("Dog")
    new_list = list(blanks(word))
    guess = ""

    while tries >= 0:
        guess = get_guess(guess)
        new_list, tries = check_guess(guess, word, new_list, tries)
        show_diagram(tries, new_list)
        checkwin(tries, new_list)

if __name__ == "__main__":
    main()

