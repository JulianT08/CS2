'''
string_manipulation.py

Description: This module contains functions to manipulate strings. 

Log: 1.0


'''
import sys
def is_string(word):
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ "
    for letter in word:
        if letter not in letters:
            return False
    return True
        
def pick_action(word):
    print('''
1. Reverse word
2. Determine number of vowels
3. Determine number of consonants   
4. Return first name
5. Check if a word is alpha (True/False)
19. Exit
20. Enter new word
          ''')
    action = int(input("Enter the number of the action you want to perform: "))
    if action == 1:
        print(reverse_string(word))
    elif action == 2:
        print(count_vowels(word))
    elif action == 3:
        print(count_consonants(word))
    elif action == 4:
        print(first_name(word))
    elif action == 5:
        print(is_string(word))
    elif action == 19:
        sys.exit()
    elif action == 20:
        word = str(input("Enter a word: "))
        return word     
def reverse_string(word):
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
            if is_string(word) == False:
                raise ValueError("Input must be a string containing only letters.")
            new_word = []
            for i in range(len(word)):
                new_word.insert(0, word[i])
            return("".join(new_word))
        except ValueError as e:
            print(e)
def count_vowels(word):
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
            if is_string(word) == False:
                raise ValueError("Input must be a string containing only letters.")
            vowels = "aeiouAEIOU"
            count = 0
            for char in word:
                if char in vowels:
                    count += 1
            return(count)
        except ValueError as e:
            print(e)
def count_consonants(word):
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
            if is_string(word) == False:
                raise ValueError("Input must be a string containing only letters.")
            vowels = "aeiouAEIOU"
            count = 0
            for char in word:
                if char not in vowels:
                    count += 1
            return(count)
        except ValueError as e:
            print(e)
def first_name(word):
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
        first_name = []
        for i in range(len(word)):
            if word[i] == " ":
                break
            else:
                first_name.append(word[i])
        return("".join(first_name))


def main():
    word = str(input("Enter a word: "))
    while True:
        word = pick_action(word)
if __name__ == "__main__":
    main()

