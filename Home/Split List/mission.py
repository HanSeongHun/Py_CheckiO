def split_list(items: list) -> list:
    # your code here
    a = len(items)
    result = [0, 0]
    first = []
    second = []
    s = 0
    if a % 2 == 1:
        s = a // 2 + 1
        first = items[:s]
        second = items[s:]
    else:
        s = a // 2
        first = items[:s]
        second = items[s:]
    result[0] = first
    result[1] = second
    return result


if __name__ == '__main__':
    print("Example:")
    print(split_list([1, 2, 3, 4, 5, 6]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert split_list([1, 2, 3, 4, 5, 6]) == [[1, 2, 3], [4, 5, 6]]
    assert split_list([1, 2, 3]) == [[1, 2], [3]]
    assert split_list([1, 2, 3, 4, 5]) == [[1, 2, 3], [4, 5]]
    assert split_list([1]) == [[1], []]
    assert split_list([]) == [[], []]
    print("Coding complete? Click 'Check' to earn cool rewards!")
