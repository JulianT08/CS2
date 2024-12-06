'''
Name: toub_julian_hangman


Log: 1
'''

def show_diagram(tries, word, guess, new_list):
    if tries == 6:
        diagram = f'''

    The word is {check_guess(guess, word, new_list, tries)}
        
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

    The word is {check_guess(guess, word, new_list, tries)}

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

    The word is {check_guess(guess, word, new_list, tries)}

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

    The word is {blanks(word)}

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

    The word is {blanks(word)}

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

    The word is {blanks(word)}

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

    The word is {blanks(word)}
  
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
    #return tries
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
    #for letter in split_word:
        #if letter == guess:
            #new_list = blanks(word).replace("_ ", guess)
            #print(new_list)
    for i in range(len(split_word)):
        if split_word[i] == guess:
            new_list[i] = guess
        else:
            tries -= 1/3
    return (" ".join(new_list)), tries

def main():
    tries = 6 #the user gets 6 initial attempts
    word = str.lower("Dog")
    new_list = list(blanks(word))
    guess = ""

    while tries > 0:
        #show_diagram(tries, word, guess, new_list)
        guess = get_guess(guess)
        show_diagram(tries, word, guess, new_list)

if __name__ == "__main__":
    main()

## LEFT OFF: currently i am trying to subtract one from tries, it is not working.
## It keeps setting tries back to 6. 
