__author__ = 'mokkeee'

import datetime

def to_date(date):
    return datetime.date(date[0], date[1], date[2])

def days_diff(date1, date2):
    d1 = to_date(date1)
    d2 = to_date(date2)
    return abs((d2 - d1).days)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert days_diff((1982, 4, 19), (1982, 4, 22)) == 3
    assert days_diff((2014, 1, 1), (2014, 8, 27)) == 238
    assert days_diff((2014, 8, 27), (2014, 1, 1)) == 238