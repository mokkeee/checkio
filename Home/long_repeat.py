#!/usr/bin/env python
# -*- coding: utf-8 -*-


def long_repeat(line):
    repeats = {None: ''}
    for char in set(line):
        for i in range(1, len(line)+1):
            repeat_chars = char * i
            if line.find(repeat_chars) >= 0:
                repeats[char] = repeat_chars
            else:
                break
    return max([len(x) for x in repeats.values()])


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    assert long_repeat('abababaab') == 2, "Third"
    assert long_repeat('') == 0, "Empty"
    assert long_repeat('aa') == 2, "Empty"
    print('"Run" is good. How is "Check"?')
