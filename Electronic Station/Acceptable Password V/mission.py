def is_acceptable_password(password: str) -> bool:
    l_result = False
    t_result = False
    s_result = False
    p_result = False
    result = False
    if len(password) > 6:
        l_result = True
    for i in password:
        if i.isdigit():
            t_result = True
        if i.isalpha():
            s_result = True
    if t_result == False:
        if len(password) > 9:
            t_result = True

    if l_result == True and t_result == True and s_result == True:
        result = True
    if 'password' in password or 'PASSWORD' in password:
        result = False

    return result


if __name__ == '__main__':
    print("Example:")
    print(is_acceptable_password('short'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_acceptable_password('short') == False
    assert is_acceptable_password('short54') == True
    assert is_acceptable_password('muchlonger') == True
    assert is_acceptable_password('ashort') == False
    assert is_acceptable_password('muchlonger5') == True
    assert is_acceptable_password('sh5') == False
    assert is_acceptable_password('1234567') == False
    assert is_acceptable_password('12345678910') == False
    assert is_acceptable_password('password12345') == False
    assert is_acceptable_password('PASSWORD12345') == False
    assert is_acceptable_password('pass1234word') == True
    print("Coding complete? Click 'Check' to earn cool rewards!")
