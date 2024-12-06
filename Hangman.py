'''
Name: toub_julian_hangman


Log: 1
'''
tries = 6
word = str.lower("Dog")
def show_diagram(tries):

    if tries == 6:
        diagram = '''
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
        diagram = '''
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
        diagram = '''
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
        diagram = '''
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
        diagram = '''
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
        diagram = '''
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
        diagram = '''
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
def check_guess(guess):
    split_word = list(word)
    for letter in split_word:
        if letter == guess:
            word_list = ['']
            word_list.append(letter)
            print(word_list)
    return word_list








def main():
    guess = get_guess()
    check_guess(guess)

if __name__ == "__main__":
    main()