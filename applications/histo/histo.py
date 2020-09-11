from collections import OrderedDict

DELETE_CHARS = "\" : ; , . - + = / \ | [ ] { } ( ) * ^ &".split()

# reuse the word count function
def word_count(s):
    count = {}
    words = sorted(s.split())
    for word in words:
        word = word.lower()
        for i in DELETE_CHARS:
            word = word.replace(i,"")
        if word != "":
            if word not in count:
                count[word] = 0
            count[word] += 1
    return count

# read in the file
with open("applications/histo/robin.txt") as f:
    words = f.read()

# pass the file into the function to get the dictonary.
dictionary = word_count(words)

def print_hist(dictionary):
    # Sort the dictionary by value
    dictionary_sorted = sorted(dictionary.items(), key=lambda x: x[1], reverse=True)
    # print out the histogram
    for item in dictionary_sorted:
        print('{k: <17}: {a}'.format(k=item[0],a="#"*item[1]))

print_hist(dictionary)