DELETE_CHARS = "\" : ; , . - + = / \ | [ ] { } ( ) * ^ &".split()

def word_count(s):
    count = {}
    words = s.split()
    for word in words:
        word = word.lower()
        for i in DELETE_CHARS:
            word = word.replace(i,"")
        if word != "":
            if word not in count:
                count[word] = 0
            count[word] += 1
    return count


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))