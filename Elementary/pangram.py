__author__ = 'mokkeee'

import string

def check_pangram(text):
    lower_ascii_chars = sorted(set(filter(lambda x: x in string.ascii_lowercase, text.lower())))
    return ''.join(lower_ascii_chars) == string.ascii_lowercase

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert check_pangram("The quick brown fox jumps over the lazy dog."), "brown fox"
    assert not check_pangram("ABCDEF"), "ABC"
    assert check_pangram("Bored? Craving a pub quiz fix? Why, just come to the Royal Oak!"), "Bored?"

