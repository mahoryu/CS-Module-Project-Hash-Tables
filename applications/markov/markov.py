import random

# Read in all the words in one go
with open("applications/markov/input.txt") as f:
    words = f.read()

"""
- create a dictonary with the word as the key, and a list of all
    possible words that could follow it.
    - loop through the input to create the dict.
    - use append to add the next word to the list
- make sure watch for stop words when printing (.!?)
- use the random to get random words from the dict lists
"""

# analyze which words can follow other words
word_list = words.split()
word_dict = {}

# create a dictonary with the word as the key, and a list of all
#    possible words that could follow it.
for i in range(len(word_list)-1):
    # if not in the dict add it else add the next word to the end of
    # the list
    if word_list[i] not in word_dict:
        word_dict[word_list[i]] = [word_list[i+1]]
    else:
        word_dict[word_list[i]].append(word_list[i+1])

# construct 5 random sentences
for _ in range(5):
    current_word = random.choice(list(word_dict.keys()))
    # set a marker to end the loop
    continue_loop = True
    while continue_loop:
        print(current_word, end= " ")
        current_word = random.choice(word_dict[current_word])
        # check the last char to see if stop word
        last_char = current_word[-1]
        if last_char == "." or last_char == "!" or last_char == "?":
            print(current_word, end= " ")
            continue_loop = False
        # if ends in a " check if the previous char is a stop.
        elif last_char == "\"":
            sec_last_char = current_word[-2]
            if sec_last_char == "." or sec_last_char == "!" or sec_last_char == "?":
                print(current_word, end= " ")
                continue_loop = False
    print()
    print()