'''
toub_julian_string_manipulation.py

Description: This module contains functions to manipulate strings. 

Log: 1.0


'''
import sys
import random
def is_string(word):
    letters = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ- ")
    for i in word:
        if i not in letters:
            return False
    return True
        
def pick_action(word, firstname, lastname, middlename):
    '''
    Acts as a menu for the user to pick the function or enter a new word. 

    Args:
        word(str): The universal word.
    
    Returns:
        word(str): The universal word.  

    Raises:
        none 
    '''
    print('''
1. Reverse word
2. Print number of vowels
3. Print number of consonants   
4. Print first name
5. Print last name
6. Print middle name (if there is one)
7. Check for hyphenated last name
8. Print lowercase version of word
9. Print uppercase version of word
10. Shuffle the letters of the word
11. Check if the word is a palindrome 
12. Print initials
18. Check if a word is valid, as in made up of letters 
19. Exit
20. Enter new word
          ''')
    action = ""
    options = '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20'
    while action not in options:
        action = input("Enter the number of the action you want to perform (1-20): ")
    action = int(action)
    if action == 1:
        print(reverse_string(word)[0])
    elif action == 2:
        print(f"Number of Vowels: {count_vowels(word)[0]}  |  A: {count_vowels(word)[1]},   E: {count_vowels(word)[2]},   I: {count_vowels(word)[3]},   O: {count_vowels(word)[4]},   U: {count_vowels(word)[5]} ")
    elif action == 3:
        consonants_count = count_consonants(word)
        print(f"Number of Consonants: {consonants_count[0]}  |  B: {consonants_count[1]},   C: {consonants_count[2]},   D: {consonants_count[3]},   F: {consonants_count[4]},   G: {consonants_count[5]},   H: {consonants_count[6]},   J: {consonants_count[7]},   K: {consonants_count[8]},   L: {consonants_count[9]},   M: {consonants_count[10]},   N: {consonants_count[11]},   P: {consonants_count[12]},   Q: {consonants_count[13]},   R: {consonants_count[14]},   S: {consonants_count[15]},   T: {consonants_count[16]},   V: {consonants_count[17]},   W: {consonants_count[18]},   X: {consonants_count[19]},   Y: {consonants_count[20]},   Z: {consonants_count[21]}")
    elif action == 4:
        print(first_name(word)[0])
    elif action == 5:
        print(last_name(word)[0])
    elif action == 6:
        print(middle_name(word, first_name, last_name)[0])
    elif action == 7:
        print(contains_hyphen(lastname))
    elif action == 8:
        print(make_lower(word)[0])
    elif action == 9:
        print(make_upper(word)[0])
    elif action == 10:
        print(mix_up(word)[0])
    elif action == 11:
        print(palindrome(word))
    elif action == 12:
        print(initials(word, firstname, lastname, middlename)[0])
    elif action == 18:
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
        word(str): The universal word.
    Returns:
        new_word(list): Reversed string.

    Raises:
        ValueError: If the input is not a string.
    '''
    while True:
        try:
            if not is_string(word):
                raise ValueError("Input must be a string containing only letters.")
            new_word = []
            for i in range(len(word)):
                new_word.insert(0, word[i])
            return ("".join(new_word)), word
        except ValueError as e:
            print(e)

def count_vowels(word):
    '''
    Counts the vowels. 

    Args:
        word(str): The universal word.
    Returns:
        count(list): The number of vowels in the string.

    Raises:
        ValueError: If the input is not a string.
    '''
    while True:
        a = 0
        e = 0
        i = 0
        o = 0
        u = 0
        try:
            if not is_string(word):
                raise ValueError("Input must be a string containing only letters.")
            vowels = "aeiouAEIOU"
            count = 0
            for char in word:
                if char in vowels:
                    count += 1
                    if char == 'a' or char == "A":
                        a += 1
                    elif char == 'e' or char == 'E':
                        e += 1
                    elif char == 'i' or char == "I":
                        i += 1
                    elif char == 'o' or char == "O":
                        o += 1
                    elif char == 'u' or char == "U":
                        u += 1
            return count, a, e, i, o, u, word
        except ValueError as e:
            print(e)

def count_consonants(word):
    '''
    Counts the consonants. 

    Args:
        word(str): The universal word.
    Returns:
        count(list): The number of consonants in the string.

    Raises:
        ValueError: If the input is not a string.
    '''
    while True:
        b = 0
        c = 0
        d = 0
        f = 0
        g = 0
        h = 0
        j = 0
        k = 0
        l = 0
        m = 0
        n = 0
        p = 0
        q = 0
        r = 0
        s = 0
        t = 0
        v = 0
        w = 0
        x = 0
        y = 0
        z = 0
        try:
            if not is_string(word):
                raise ValueError("Input must be a string containing only letters.")
            vowels = "aeiouAEIOU"
            count = 0
            for char in word:
                if char not in vowels:
                    count += 1
                    if char == 'b' or char == "B":
                        b += 1
                    elif char == 'c' or char == 'C':
                        c += 1
                    elif char == 'd' or char == "D":
                        d += 1
                    elif char == 'f' or char == "F":
                        f += 1
                    elif char == 'g' or char == "G":
                        g += 1
                    elif char == 'h' or char == "H":
                        h += 1
                    elif char == 'j' or char == "J":
                        j += 1
                    elif char == 'k' or char == "K":
                        k += 1
                    elif char == 'l' or char == "L":
                        l += 1
                    elif char == 'm' or char == "M":
                        m += 1
                    elif char == 'n' or char == "N":
                        n += 1
                    elif char == 'p' or char == "P":
                        p += 1
                    elif char == 'q' or char == "Q":
                        q += 1
                    elif char == 'r' or char == "R":
                        r += 1
                    elif char == 's' or char == "S":
                        s += 1
                    elif char == 't' or char == "T":
                        t += 1
                    elif char == 'v' or char == "V":
                        v += 1
                    elif char == 'w' or char == "W":
                        w += 1
                    elif char == 'x' or char == "X":
                        x += 1
                    elif char == 'y' or char == "Y":
                        y += 1
                    elif char == 'z' or char == "Z":
                        z += 1
            return count, b, c, d, f, g, h, j, k, l, m, n, p, q, r, s, t, v, w, x, y, z, word
        except ValueError as e:
            print(e)

def first_name(word):
    '''
    Returns the first name. 

    Args:
        word(str): The universal word.

    Returns:
        first_name(str): The first name.

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
        return "".join(first_name), word

def last_name(word):
    '''
    Returns the last name. 

    Args:
        word(str): The universal word.

    Returns:
        last_name(str): The last name.

    Raises:
        none 
    '''
    name = word.split()
    if len(name) > 1:
        last_name = name[-1]
    else:
        last_name = word
    return "".join(last_name), word

def middle_name(word, first_name, last_name):
    '''
    Returns the middle name. 

    Args:
        word(str): The universal word.
    Returns:
        middle_name(str): The middle name(s).

    Raises:
        none 
    '''

    broken_word = word.split()
    if first_name(word)[0] in broken_word:
        broken_word.remove(first_name(word)[0])
    if last_name(word)[0] in broken_word:
        broken_word.remove(last_name(word)[0])
    middle_name = " ".join(broken_word)
    return middle_name, word

def contains_hyphen(lastname):
    if '-' in lastname:
        return True
    else:
        return False

def make_lower(word):
    '''
    Prints the lowercase version of the word. 

    Args:
        word(str): The universal word.

    Returns:
        lower_word(str): The word in lowercase.
        word(str): The universal word.

    Raises:
        none 
    '''    
    lower_word = []
    for i in range(len(word)):
        letter = ord(word[i])
        if letter >= 65 and letter <= 90:
            lower_word.append(chr(letter + 32))
        else:
            lower_word.append(chr(letter))
    return "".join(lower_word), word

def make_upper(word):
    '''
    Prints the uppercase version of the word. 

    Args:
        word(str): The universal word.

    Returns:
        upper_case(str): The word in lowercase.
        word(str): The universal word.

    Raises:
        none 
    '''    
    upper_word = []
    for i in range(len(word)):
        letter = ord(word[i])
        if letter >= 97 and letter <= 122:
            upper_word.append(chr(letter - 32))
        else:
            upper_word.append(chr(letter))
    return "".join(upper_word), word

def mix_up(word):
    '''
    Mixes up the word. 

    Args:
        word(str): The universal word.

    Returns:
        mixed_word(str): The mixed up word.
        word(str): The universal word.
        
    Raises:
        none 
    '''    
    word = list(word)
    mixed_word = []
    for i in range(len(word)):
        letter = random.choice(word)
        mixed_word.append(letter)
        word.remove(letter)
    "".join(mixed_word), word

def palindrome(word):
    lower_word = make_lower(word)[0]
    reversed_word = reverse_string(lower_word)[0]
    return reversed_word == lower_word

def initials(word, firstname, lastname, middle_name):
    initial1 = list(firstname)[0]
    initial2 = list(lastname)[0]
    initials = (make_upper(initial1)[0], make_upper(initial2)[0])
    return ("".join(initials)), word



def main():
    word = str(input("Enter a word: "))
    firstname = first_name(word)[0] # Not used, but available
    lastname = last_name(word)[0] # Derrive last name from word
    middlename = middle_name(word, first_name, last_name)[0]
    while True:
        word = pick_action(word, firstname, lastname, middlename)
        lastname = last_name(word)[0] # Update last name


if __name__ == "__main__":
    main()
