#!/usr/bin/env python
# -*- coding: utf-8 -*-

MAX_BIN_LEN = len(format(10 ** 6, 'b'))


def to_bin_list(num: int):
    return [int(x) for x in list(format(num, 'b').zfill(MAX_BIN_LEN))]


def checkio(num1: int, num2: int):
    num1_bin = to_bin_list(num1)
    num2_bin = to_bin_list(num2)

    diff_count = 0
    for x1, x2 in zip(num1_bin, num2_bin):
        if x1 ^ x2 == 1:
            diff_count += 1

    return diff_count


def checkio_use_numpy(num1: int, num2: int):
    num1_bin = to_bin_list(num1)
    num2_bin = to_bin_list(num2)

    import numpy as np
    xor = list(np.logical_xor(num1_bin, num2_bin))
    return xor.count(1)


if __name__ == '__main__':
    assert checkio(117, 17) == 3
    assert checkio(1, 2) == 2
    assert checkio(16, 15) == 5

    assert checkio_use_numpy(117, 17) == 3
    assert checkio_use_numpy(1, 2) == 2
    assert checkio_use_numpy(16, 15) == 5
