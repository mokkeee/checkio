import string

def checkio(text):
    text = text.lower().strip()
    char_and_count = {}
    for c in string.ascii_lowercase:
        char_and_count[c] = text.count(c)
    
    max_count = max(char_and_count.values())
    max_count_chars = {k:v for (k,v) in char_and_count.items() if v == max_count }
    
    return min(max_count_chars.keys())

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
