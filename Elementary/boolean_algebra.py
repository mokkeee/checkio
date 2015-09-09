# OPERATION_NAMES = ("conjunction", "disjunction", "implication", "exclusive", "equivalence")
OPERATIONS = {"conjunction": (lambda x, y: x & y),
              "disjunction": (lambda x, y: x | y),
              "implication": (lambda x, y: (x ^ 1) | y ),
              "exclusive": (lambda x, y: x ^ y),
              "equivalence": (lambda x, y: int(x == y))}


def boolean(x, y, operation):
    return OPERATIONS[operation](x, y)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert boolean(1, 0, "conjunction") == 0, "and"
    assert boolean(1, 0, "disjunction") == 1, "or"
    assert boolean(1, 1, "implication") == 1, "material"
    assert boolean(0, 1, "exclusive") == 1, "xor"
    assert boolean(0, 1, "equivalence") == 0, "same?"
