__author__ = 'mokkeee'


def checkio(number):
    multi_val = 1
    while number > 0:
        digit = int(number % 10)
        number //= 10
        if digit != 0:
            multi_val *= digit

    return multi_val


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1

