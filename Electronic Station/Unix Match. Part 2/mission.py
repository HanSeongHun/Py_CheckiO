def unix_match(filename: str, pattern: str) -> bool:
    if filename == pattern:
        return True
    save = []
    result = False
    start = 0
    if '[' in pattern:
        start = pattern.find('[')
        save = pattern[pattern.find('[') + 1:pattern.find(']')]
        if filename in pattern:
            return False
        if len(save) == 0:
            return False

    else:
        if filename != pattern:
            return False

    if '!' in save:
        if save.find(filename[start]) != -1:
            result = False
        else:
            result = True
    else:
        if pattern.find(filename[start]) == -1:
            result = False
        else:
            result = True
    print(save)

    return result


if __name__ == '__main__':
    print("Example:")

    # These "asserts" are used for self-checking and not for an auto-testing
    assert unix_match("nametxt", "name[]txt") == True
    print("Coding complete? Click 'Check' to earn cool rewards!")
