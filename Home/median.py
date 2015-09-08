__author__ = 'mokkeee'


def checkio(data):
    #replace this for solution
    data = sorted(data)
    # print(data)

    med_idx = int(len(data) / 2)
    # print(med_idx)
    if len(data) % 2 == 1:
        # print('奇数')
        return data[med_idx]
    else:
        # print('偶数')
        even_list = data[med_idx-1:med_idx+1]
        # print(even_list)
        return sum(even_list) / 2

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([1, 2, 3, 4, 5]) == 3, "Sorted list"
    assert checkio([3, 1, 2, 5, 3]) == 3, "Not sorted list"
    assert checkio([1, 300, 2, 200, 1]) == 2, "It's not an average"
    assert checkio([3, 6, 20, 99, 10, 15]) == 12.5, "Even length"
