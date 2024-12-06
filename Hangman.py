'''
Name: toub_julian_hangman


Log: 1
'''

def show_diagram(tries, word):
    if tries == 6:
        diagram = f'''

    The word is {blanks(word)}
        
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

    The word is {blanks(word)}

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

    The word is {blanks(word)}

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
    return diagram
def get_guess(guess):
    while True:
        guess = str.lower(input("Enter your guess: "))
        if guess.isalpha():
            return guess
        else:
            print("Guess must be a letter. (e.g. a b c ) ")
def blanks(word):
    word_list = str("_ ")*len(word)
    return word_list


def check_guess(guess, word):
    split_word = list(word)
    #for letter in split_word:
        #if letter == guess:
            #new_list = blanks(word).replace("_ ", guess)
            #print(new_list)
    new_list = blanks(word)
    for i in split_word:
        if split_word[i] == guess:
            new_list[i] = guess
            print(new_list)
    #return word_list


def main():
    tries = 6 #the user gets 6 initial attempts
    word = str.lower("Dog")
    show_diagram(tries, word)
    guess = ""
    guess = get_guess(guess)
    check_guess(guess, word)
    show_diagram(tries, word)

if __name__ == "__main__":
    main()