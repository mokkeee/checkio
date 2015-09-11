__author__ = 'mokkeee'


def checkio(number):
    num_str = str(number).replace('0', '')
    multi_val = 1
    for x in num_str:
        multi_val *= int(x)
    return multi_val


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1

