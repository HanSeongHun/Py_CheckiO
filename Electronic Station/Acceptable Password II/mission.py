def is_acceptable_password(password: str) -> bool:
    # your code here
    l_result = False
    t_result = False
    result = False
    if len(password) > 6:
        l_result = True
    for i in password:
        if i.isdigit():
            t_result = True
    print(t_result)
    if l_result == True and t_result == True:
        result = True

    return result


if __name__ == '__main__':
    print("Example:")
    print(is_acceptable_password('short'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_acceptable_password('short') == False
    assert is_acceptable_password('muchlonger') == False
    assert is_acceptable_password('ashort') == False
    assert is_acceptable_password('muchlonger5') == True
    assert is_acceptable_password('sh5') == False
    print("Coding complete? Click 'Check' to earn cool rewards!")
