__author__ = 'mokkeee'


def checkio(number):
    remainder = number
    pigeons = 0
    new_pigeons = 1

    while remainder > 0:
        remainder -= pigeons
        if remainder <= 0:
            break
        elif remainder < new_pigeons:
            pigeons += remainder
            break
        else:
            remainder -= new_pigeons
            pigeons += new_pigeons
            new_pigeons += 1

    return pigeons


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(1) == 1, "1st example"
    assert checkio(2) == 1, "2nd example"
    assert checkio(5) == 3, "3rd example"
    assert checkio(10) == 6, "4th example"
