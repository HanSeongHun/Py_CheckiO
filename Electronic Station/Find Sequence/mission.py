def check_line(line):
    if 4 <= len(line) and 4 == line[0:4].count(line[0]):
        return True


def checkio(matrix):
    # replace this for solution
    width = len(matrix[0])
    height = len(matrix)
    for y in range(height):
        for x in range(width):
            h_line = matrix[y][x:]
            if check_line(h_line):
                return True

            v_line = [matrix[r][x] for r in range(y, height)]
            if check_line(v_line):
                return True

            right_down_line = [matrix[r][c] for r, c in zip(range(y, height), range(x, width))]
            if check_line(right_down_line):
                return True

            left_down_line = [matrix[r][c] for r, c in zip(range(y, height), range(x, -1, -1))]
            if check_line(left_down_line):
                return True

    return False


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        [1, 2, 1, 1],
        [1, 1, 4, 1],
        [1, 3, 1, 6],
        [1, 7, 2, 5]
    ]) == True, "Vertical"
    assert checkio([
        [7, 1, 4, 1],
        [1, 2, 5, 2],
        [3, 4, 1, 3],
        [1, 1, 8, 1]
    ]) == False, "Nothing here"
    assert checkio([
        [2, 1, 1, 6, 1],
        [1, 3, 2, 1, 1],
        [4, 1, 1, 3, 1],
        [5, 5, 5, 5, 5],
        [1, 1, 3, 1, 1]
    ]) == True, "Long Horizontal"
    assert checkio([
        [7, 1, 1, 8, 1, 1],
        [1, 1, 7, 3, 1, 5],
        [2, 3, 1, 2, 5, 1],
        [1, 1, 1, 5, 1, 4],
        [4, 6, 5, 1, 3, 1],
        [1, 1, 9, 1, 2, 1]
    ]) == True, "Diagonal"
