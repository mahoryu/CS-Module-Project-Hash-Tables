def no_dups(s):
    lookup_table = {}
    for word in s.split():
        if word in lookup_table.keys():
            continue
        else:
            lookup_table[word] = 1
    output = ""
    for key in lookup_table:
        output += f"{key} "
    return output[:-1]

if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))