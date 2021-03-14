def unix_match(filename: str, pattern: str) -> bool:
    result = False
    if filename == pattern:
        return True

    if '*' in pattern:
        result = True
        for i in pattern:
            if i != '*':
                result = False
                if i == '.':
                    if '.' in filename:
                        result = True
                    else:
                        result = False
    if '?' in pattern:
        if '*' in pattern:
            result = True
            if pattern.count('?') > len(filename):
                result = False
                print(pattern.count('?'))
        if len(filename) == len(pattern):
            result = True

    return result


if __name__ == '__main__':
    print("Example:")
    print(unix_match('somefile.txt', '*'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert unix_match("l.txt", "???*") == True
    assert unix_match('other.exe', '*') == True
    assert unix_match('my.exe', '*.txt') == False
    assert unix_match('log1.txt', 'log?.txt') == True
    assert unix_match('log12.txt', 'log?.txt') == False
    assert unix_match('log12.txt', 'log??.txt') == True
    print("Coding complete? Click 'Check' to earn cool rewards!")
