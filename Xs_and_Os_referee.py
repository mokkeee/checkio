__author__ = 'mokkeee'


def referee(line):
    for c in "X" "O":
        if line.count(c) == line.__len__():
            return c

    return None


def referee_horizontal(game_result):
    for line in game_result:
        result = referee(line)
        if result is not None:
            return result

    return referee_vertical(game_result)


def referee_vertical(game_result):
    for j in range(game_result[0].__len__()):
        line = ""
        for i in range(game_result.__len__()):
            line += game_result[i][j]

        result = referee(line)
        if result is not None:
            return result

    return referee_slant1(game_result)


def referee_slant1(game_result):
    line = ""
    for i in range(game_result[0].__len__()):
        line += game_result[i][i]

    result = referee(line)
    if result is not None:
        return result

    return referee_slant2(game_result)


def referee_slant2(game_result):
    line = ""
    len = game_result[0].__len__()
    for i in range(len):
            line += game_result[i][len - i - 1]

    result = referee(line)
    if result is not None:
        return result

    return "D"


def checkio(game_result):
    return referee_horizontal(game_result)


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"


