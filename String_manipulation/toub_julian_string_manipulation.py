'''
toub_julian_string_manipulation.py

Description: This module contains functions to manipulate strings. 

Log: 1.0


'''
import sys

def is_string(word):
    letters = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ")
    for i in word:
        if i not in letters:
            return False
    return True
        
def pick_action(word):
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
2. Determine number of vowels
3. Determine number of consonants   
4. Return first name
5. Return last name
6. Return middle name (if there is one)
18. Check if a word is valid, as in made up of letters (True/False)
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
    last_name = name[-1]
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
    first_name = [first_name(word)[0]]
    first_name = "".join(first_name)
    last_name = [last_name(word)[0]]
    last_name = "".join(last_name)
    for word in broken_word:
        if str(word) == first_name:
            broken_word.remove(first_name)
        elif str(word) == last_name:
            broken_word.remove(last_name)
    middle_name = " ".join(broken_word)
    return middle_name, word

def main():
    word = str(input("Enter a word: "))
    while True:
        word = pick_action(word)

if __name__ == "__main__":
    main()
