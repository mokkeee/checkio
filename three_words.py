__author__ = 'mokkeee'


def checkio(words):
    word_count = 0
    for word in words.split(" "):
        #print(word)
        if word.isalpha():
            word_count += 1
            if word_count == 3:
                return True
        else:
            word_count = 0
    else:
        return False


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("Hello World hello") == True, "Hello"
    assert checkio("He is 123 man") == False, "123 man"
    assert checkio("1 2 3 4") == False, "Digits"
    assert checkio("bla bla bla bla") == True, "Bla Bla"
    assert checkio("Hi") == False, "Hi"

