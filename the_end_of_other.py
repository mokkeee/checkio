__author__ = 'mokkeee'


def checkio(words_set):
    sorted_words_set = sorted(words_set, key=len, reverse=False)
    while len(sorted_words_set) > 1:
        word = sorted_words_set.pop(0)
        for compare_set in sorted_words_set:
            if compare_set.endswith(word):
                return True
    else:
        return False


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio({"hello", "lo", "he"}) == True, "helLO"
    assert checkio({"hello", "la", "hellow", "cow"}) == False, "hellow la cow"
    assert checkio({"walk", "duckwalk"}) == True, "duck to walk"
    assert checkio({"one"}) == False, "Only One"
    assert checkio({"helicopter", "li", "he"}) == False, "Only end"

