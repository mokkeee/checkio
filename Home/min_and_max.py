#!/usr/bin/env python
# -*- coding: utf-8 -*-


def find_target(args, key, reverse):
    datum = args[0] if len(args) == 1 else args
    return sorted(datum, key=key, reverse=reverse)[0]


def min(*args, key=None):
    return find_target(args, key, False)


def max(*args, key=None):
    return find_target(args, key, True)


'''
def min(*args, key=None):
    datum_list = to_list(args)

    min_val = datum_list[0]
    for i in range(1, len(datum_list)):
        val = datum_list[i]
        if key is None:
            if min_val > val:
                min_val = val
        else:
            if key(min_val) > key(val):
                min_val = val
    return min_val

def max(*args, key=None):
    datum_list = to_list(args)

    max_val = datum_list[0]
    for i in range(1, len(datum_list)):
        val = datum_list[i]
        if key is None:
            if max_val < val:
                max_val = val
        else:
            if key(max_val) < key(val):
                max_val = val
    return max_val
'''

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert max(3, 2) == 3, "Simple case max"
    assert min(3, 2) == 2, "Simple case min"
    assert max([1, 2, 0, 3, 4]) == 4, "From a list"
    assert min("hello") == "e", "From string"
    assert max(2.2, 5.6, 5.9, key=int) == 5.6, "Two maximal items"
    assert min([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]) == [9, 0], "lambda key"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
