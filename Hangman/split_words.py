with open(r'C:/Users/jtoub26/Documents/GitHub/CS2/Hangman/words_to_use.txt', 'r') as file:
    words = file.read().split(', ')

with open(r'C:/Users/jtoub26/Documents/GitHub/CS2/Hangman/words_to_use_new.txt', 'w') as file:
    for word in words:
        file.write(word + '\n')