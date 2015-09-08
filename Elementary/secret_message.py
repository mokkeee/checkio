__author__ = 'mokkeee'


def find_message(text):
    upper_chars = filter(lambda c: c.isupper() == True, text)
    return "".join(upper_chars)


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert find_message("How are you? Eh, ok. Low or Lower? Ohhh.") == "HELLO", "hello"
    assert find_message("hello world!") == "", "Nothing"
    assert find_message("HELLO WORLD!!!") == "HELLOWORLD", "Capitals"

