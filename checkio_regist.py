__author__ = 'motegi'


def checkio(els):
    a = els[0:3]
    print(a)
    print(sum(a))
    return sum(a)


if checkio([1, 2, 3, 4, 5, 6]) == 6:
    print('Done!')
else:
    print('Fault')