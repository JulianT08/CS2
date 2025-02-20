'''
toub_julian_string_manipulation.py

Description: This module contains functions to manipulate strings. 

Features: 
- Menu to pick between functions
- Checks if the word is valid, as in made up of letters only.
- Allows the user to continuously run the program until exited.
- Sorts vowels and prints their respective frequencies. 
- Sorts consonants and prints their respecitve frequencies. 
- Sorts the full name alphabetically.
- Checks for title/distinction.
- Removes title/distintion.
- Encrypts a message.
- Decrypts a message.

Log: 1.0

'''
import sys
import random
decrypt = False

def is_string(word):
    letters = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-. ")
    for i in word:
        if i not in letters:
            return False
    return True
        
def pick_action(word, firstname, lastname, middlename, decrypt, encrypted):
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
1. Remove title/distinction        [ex. "Dr.", "Dr", "Sir", "Esq", "Ph.D"]
2. Reverse word
3. Print number of vowels
4. Print number of consonants   
5. Print first name
6. Print last name
7. Print middle name (if there is one)
8. Check for hyphenated last name
9. Print lowercase version of word
10. Print uppercase version of word
11. Shuffle the letters of the word
12. Check if the word is a palindrome 
13. Print initials
14. Sort the string alphabetically
15. Check for title/distinction    [ex. "Dr.", "Dr", "Sir", "Esq", "Ph.D"]
16. Check if a word is valid, as in made up of letters 
17. Encrypt word or message
18. Decrypt word or message (must encrypt first)
19. Enter new word/name
20. Exit
          ''')
    action = ""
    options = '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20'
    while action not in options:
        action = input("Enter the number of the action you want to perform (1-20): ")
    action = int(action)
    while True:
        if is_string(word) == True:
            if action == 1:
                word = remove_distinction(word)
            elif action == 2:
                print(reverse_string(word)[0])
            elif action == 3:
                print(f"Number of Vowels: {count_vowels(word)[0]}  |  A: {count_vowels(word)[1]},   E: {count_vowels(word)[2]},   I: {count_vowels(word)[3]},   O: {count_vowels(word)[4]},   U: {count_vowels(word)[5]} ")
            elif action == 4:
                consonants_count = count_consonants(word)
                print(f"Number of Consonants: {consonants_count[0] > 0, }  |  B: {consonants_count[1]},   C: {consonants_count[2]},   D: {consonants_count[3]},   F: {consonants_count[4]},   G: {consonants_count[5]},   H: {consonants_count[6]},   J: {consonants_count[7]},   K: {consonants_count[8]},   L: {consonants_count[9]},   M: {consonants_count[10]},   N: {consonants_count[11]},   P: {consonants_count[12]},   Q: {consonants_count[13]},   R: {consonants_count[14]},   S: {consonants_count[15]},   T: {consonants_count[16]},   V: {consonants_count[17]},   W: {consonants_count[18]},   X: {consonants_count[19]},   Y: {consonants_count[20]},   Z: {consonants_count[21]}")
            elif action == 5:
                print(first_name(word)[0])
            elif action == 6:
                print(last_name(word)[0])
            elif action == 7:
                print(middle_name(word, first_name, last_name)[0])
            elif action == 8:
                print(contains_hyphen(lastname))
            elif action == 9:
                print(make_lower(word)[0])
            elif action == 10:
                print(make_upper(word)[0])
            elif action == 11:
                print(mix_up(word)[0])
            elif action == 12:
                print(palindrome(word))
            elif action == 13:
                print(initials(word)[0])
            elif action == 14:
                print(sort_word(word))
            elif action == 15:
                print(check_distinction(word))
            elif action == 16:
                print(is_string(word))
            elif action == 17:
                print(encrypt_word(word))
                encrypted = encrypt_word(word)
                decrypt = True
            elif action == 18 and decrypt == True:
                print(decrypt_word(encrypted))
            elif action == 18 and decrypt == False:
                print("Must encrypt message before decrypting. ")
            elif action == 19:
                word = str(input("Enter a word or name: "))
            elif action == 20:
                sys.exit()
            return word, decrypt
        else:
            print("Must be a word.")
            word = str(input("Enter a word: "))


def reverse_string(word):
    '''
    Reverses a string. 

    Args:
        word(str): The universal word.

    Returns:
        new_word(list): Reversed string.
        word(str): The universal word. 

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
        word(str): The universal word. 

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
        word(str): The universal word. 

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
        word(str): The universal word. 

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
    '''
    Checks if the last name contains a hyphen.

    Args:
        lastname(str): The last name.

    Returns:
        bool: True if the last name contains a hyphen, False otherwise.

    Raises:
        none 
    '''
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
    for letter in range(len(word)):
        letter = random.choice(word)
        mixed_word.append(letter)
        word.remove(letter)
    return "".join(mixed_word), word

def palindrome(word):
    '''
    Checks if the given word is a palindrome.

    Args:
        word(str): The universal word.

    Returns:
        bool: True if the word is a palindrome, False otherwise.

    Raises:
        none 
    '''    
    lower_word = make_lower(word)[0]
    reversed_word = reverse_string(lower_word)[0]
    return reversed_word == lower_word

def initials(word):
    '''
    Returns the initials of every word. 
    
    Args:
        word(str): The universal word.

    Returns:
        initial(str): The initials.
        word(str): The universal word. 

    Raises:
        none 
    '''
    initials = []
    for word in word.split(" "):     
        initials.append(word[0])
    initials = make_upper("".join(initials))[0]
    return initials, word

def sort_word(word):
    '''
    Sorts the word alphabetically. 
    
    Args:
        word(str): The universal word.

    Returns:
        broken_word: The sorted word.

    Raises:
        none 
    '''
    broken_word = list(word)
    broken_word.sort()
    sorted_word = "".join(broken_word)
    return sorted_word

def check_distinction(word):
    if "Dr." or "Dr" or "Sir" or "Esq" or "Ph.D" in word.split():
        return True
    else:
        return False

def remove_distinction(word):
    distinctions = ["Dr.", "Dr", "Sir", "Esq", "Ph.D"]
    words = word.split()
    result = []
    for i in words:
        if i not in distinctions:
            result.append(i)
    return " ".join(result)

def encrypt_word(word):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    symbols = ['1','0','2','9','3','8','4','7','6','!',"/","?","|","[","{","]","}","+","=","$","<",">","@","%","^","-"]
    word = make_lower(word)[0]
    encrypted = ""
    for char in word:
        if char in letters:
            index = letters.index(char)
            encrypted += symbols[index]
        else:
            encrypted += char
    return encrypted

def decrypt_word(encrypted):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    symbols = ['1','0','2','9','3','8','4','7','6','!',"/","?","|","[","{","]","}","+","=","$","<",">","@","%","^","-"]
    decrypted = ""
    for char in encrypted:
        if char in symbols:
            index = symbols.index(char)
            decrypted += letters[index]
        else:
            decrypted += char
    return decrypted

def main():
    word = str(input("Enter a word: "))
    decrypt = False
    firstname = first_name(word)[0]
    lastname = last_name(word)[0]
    middlename = middle_name(word, first_name, last_name)[0]
    encrypted = encrypt_word(word)

    while True:
        word, decrypt = pick_action(word, firstname, lastname, middlename, decrypt, encrypted) # Asks for the word/name and then the action
        firstname = first_name(word)[0] # Updates first name
        middlename = middle_name(word, first_name, last_name)[0] # Updates middle name
        lastname = last_name(word)[0] # Updates last name


if __name__ == "__main__":
    main()
