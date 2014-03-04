__author__ = 'mokkeee'


def roman_num(num, base, base5, upper):
    assert 0 <= num <= 9

    if num == 0:
        return ""
    elif num <= 3:
        return base * num
    elif num == 4:
        return base + base5
    elif num == 5:
        return base5
    elif num <= 8:
        return base5 + (base * (num-5))

    return base + upper


def checkio(data):
    symbols = (("I", "V"), ("X", "L"), ("C", "D"), "M")

    if data < 10:
        return roman_num(data, symbols[0][0], symbols[0][1], symbols[1][0])
    elif data < 100:
        return roman_num(data // 10, symbols[1][0], symbols[1][1], symbols[2][0]) + checkio(data % 10)
    elif data < 1000:
        return roman_num(data // 100, symbols[2][0], symbols[2][1], symbols[3][0]) + checkio(data % 100)
    else:
        return roman_num(data // 1000, symbols[3][0], "", "") + checkio(data % 1000)


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(6) == 'VI', '6'
    assert checkio(76) == 'LXXVI', '76'
    assert checkio(499) == 'CDXCIX', '499'
    assert checkio(3889) == 'MMMDCCCLXXXVIII', '3888'
