'''
string_manipulation.py

Description: This module contains functions to manipulate strings. 

Log: 1.0


'''
import sys
def pick_action():
    print('''
1. Reverse String
2. Determine number of vowels
3. Determine number of consonants   
4. Return first name
19. Exit
          ''')
    action = int(input("Enter the number of the action you want to perform: "))
    if action == 1:
        print(reverse_string())
    elif action == 2:
        print(count_vowels())
    elif action == 3:
        print(count_consonants())
    elif action == 4:
        print(first_name())
    elif action == 19:
        sys.exit()
def reverse_string():
    '''
    Reverses a string. 

    Args:
        none.
    Returns:
        new_word(list): Reversed string

    Raises:
        ValueError: If the input is not a string. 
    '''
    while True:
        try:
            word = input("Enter a word: ")
            if not word.isalpha():
                raise ValueError("Input must be a string containing only letters.")
            new_word = []
            for i in range(len(word)):
                new_word.insert(0, word[i])
            print("".join(new_word))
            break
        except ValueError as e:
            print(e)
def count_vowels():
    '''
    Counts the vowels. 

    Args:
        none.
    Returns:
        count(list): The nuber of vowels in the string

    Raises:
        ValueError: If the input is not a string. 
    '''
    while True:
        try:
            word = input("Enter a word: ")
            if not word.isalpha():
                raise ValueError("Input must be a string containing only letters.")
            vowels = "aeiouAEIOU"
            count = 0
            for char in word:
                if char in vowels:
                    count += 1
            return(count)
        except ValueError as e:
            print(e)
def count_consonants():
    '''
    Counts the consonants. 

    Args:
        none.
    Returns:
        count(list): The nuber of consonants in the string

    Raises:
        ValueError: If the input is not a string. 
    '''
    while True:
        try:
            word = input("Enter a word: ")
            if not word.isalpha():
                raise ValueError("Input must be a string containing only letters.")
            vowels = "aeiouAEIOU"
            count = 0
            for char in word:
                if char not in vowels:
                    count += 1
            return(count)
        except ValueError as e:
            print(e)
def first_name():
    '''
    Returns the first name. 

    Args:
        none.
    Returns:
        first_name(str): The first name

    Raises:
        none 
    '''
    while True:
        word = input("Enter your name: ")
        first_name = []
        for i in range(len(word)):
            if word[i] == " ":
                break
            else:
                first_name.append(word[i])
        return("".join(first_name))


def main():
    pick_action()
    sys.exit()
if __name__ == "__main__":
    main()