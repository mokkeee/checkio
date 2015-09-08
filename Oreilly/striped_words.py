__author__ = 'mokkeee'

import re

VOWELS = "AEIOUY"
CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ"


def check_stripe(word, even, add):
    for i in range(0, len(word), 2):
        if even.find(word[i]) == -1:
            return False
    for i in range(1, len(word), 2):
        if add.find(word[i]) == -1:
            return False
    else:
        return True


def checkio(text):
    count = 0
    for word in re.split(' |,|\.|\?|!', text):
        if len(word) <= 1:
            continue
        word = word.upper()
        # check stripe word (start vowels char)
        if check_stripe(word, VOWELS, CONSONANTS):
            count += 1
        # check stripe word (start consonants char)
        elif check_stripe(word, CONSONANTS, VOWELS):
            count += 1

    return count

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("My name is ...") == 3, "All words are striped"
    assert checkio("Hello world") == 0, "No one"
    assert checkio("A quantity of striped words.") == 1, "Only of"
    assert checkio("Dog,cat,mouse,bird.Human.") == 3, "Dog, cat and human"

