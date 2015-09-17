__author__ = 'mokkeee'


def is_enable(grid, row, col):
    if row < 0 or col < 0:
        return False
    if row >= len(grid):
        return False
    if col >= len(grid[row]):
        return False
    return True

def get_neighbour(grid, row, col):
    if not is_enable(grid, row, col):
        return None
    return grid[row][col]


def count_neighbours(grid, row, col):
    neighbours = []
    for r in range(row - 1, row + 2):
        for c in range(col - 1, col + 2):
            if r == row and c == col:
                continue
            neighbours.append(get_neighbour(grid, r, c))

    # print(neighbours)
    return neighbours.count(1)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_neighbours(((1, 0, 0, 1, 0),
                             (0, 1, 0, 0, 0),
                             (0, 0, 1, 0, 1),
                             (1, 0, 0, 0, 0),
                             (0, 0, 1, 0, 0),), 1, 2) == 3, "1st example"
    assert count_neighbours(((1, 0, 0, 1, 0),
                             (0, 1, 0, 0, 0),
                             (0, 0, 1, 0, 1),
                             (1, 0, 0, 0, 0),
                             (0, 0, 1, 0, 0),), 0, 0) == 1, "2nd example"
    assert count_neighbours(((1, 1, 1),
                             (1, 1, 1),
                             (1, 1, 1),), 0, 2) == 3, "Dense corner"
    assert count_neighbours(((0, 0, 0),
                             (0, 1, 0),
                             (0, 0, 0),), 1, 1) == 0, "Single"
