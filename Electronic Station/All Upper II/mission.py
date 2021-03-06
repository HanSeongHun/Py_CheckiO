def is_all_upper(text: str) -> bool:
    result = True
    text = text.replace(" ", "")
    if len(text) == 0:
        return False
    if text.isdigit():
        return Fal
    for i in text:
        if i.islower():
            result = False
    return result


if __name__ == '__main__':
    print("Example:")
    print(is_all_upper('ALL UPPER'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_all_upper('123') == True
    assert is_all_upper('all lower') == False
    assert is_all_upper('mixed UPPER and lower') == False
    assert is_all_upper('') == False
    print("Coding complete? Click 'Check' to earn cool rewards!")
