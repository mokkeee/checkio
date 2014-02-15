__author__ = 'mokkeee'

FIRST_TEN = ["zero", "one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = "hundred"


def checkio(number):
    if number < 10:
        numeric_str = FIRST_TEN[number]
    elif number < 100:
        if number < 20:
            return SECOND_TEN[number - 10]
        else:
            tens_number = int(number / 10)
            numeric_str = ' '.join((OTHER_TENS[tens_number - 2], checkio(number % 10)))
    else:
        hundred_number = int(number / 100)
        numeric_str = ' '.join((checkio(hundred_number), HUNDRED, checkio(number % 100)))

    if numeric_str.endswith(' ' + FIRST_TEN[0]):
        numeric_str = numeric_str.replace(' ' + FIRST_TEN[0], '')

    # print(numeric_str)
    return numeric_str


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(4) == 'four', "1st example"
    assert checkio(133) == 'one hundred thirty three', "2nd example"
    assert checkio(12) == 'twelve', "3rd example"
    assert checkio(101) == 'one hundred one', "4th example"
    assert checkio(212) == 'two hundred twelve', "5th example"
    assert checkio(40) == 'forty', "6th example"

