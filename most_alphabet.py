__author__ = 'motegi'
import string

def checkio(text):
    text = text.lower().strip()
    char_and_count = []
    for c in string.ascii_lowercase:
        char_count = text.count(c)
        if char_count != 0:
            char_and_count.append((c, char_count))
    char_and_count.sort(key=lambda count: count[1], reverse=True)

    print(char_and_count)

    return char_and_count[0][0]

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
