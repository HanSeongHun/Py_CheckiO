def checkio(text: str) -> str:
    # replace this for solution
    text = text.lower()
    text = sorted(text)
    i = 0
    check = []
    sol = 0
    for t in text:
        if t.isalpha():
            check.append(t)

    if len(check) == 1:
        return check[0]

    i = 0
    temp = check.count(check[0])
    while True:
        if check[i] != check[i + 1]:
            if check.count(check[sol]) < check.count(check[i + 1]):
                sol = i + 1
        i = i + 1

        if i + 1 == len(check):
            break

    print(sol)

    return check[sol]


if __name__ == '__main__':
    print("Example:")
    print(checkio("Hello World!"))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")
