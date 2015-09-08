__author__ = 'mokkeee'
import string

def is_contains(chk_data, contains_chars):
    for c in contains_chars:
        if chk_data.find(c) != -1:
            return True

    return False

def checkio(data):

    #replace this for solution
    #check symbols
    sym = set(data)
    if len(sym) < 10:
        return False

    if not is_contains(data, string.digits):
        return False

    if not is_contains(data, string.ascii_lowercase):
        return False

    if not is_contains(data, string.ascii_uppercase):
        return False

    return True

#Some hints
#Just check all conditions


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"