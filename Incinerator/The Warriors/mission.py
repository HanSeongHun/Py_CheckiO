class Warrior:
    health = 50
    attack = 5
    is_alive = True


class Knight(Warrior):
    health = 50
    attack = 7
    is_alive = True


def fight(unit_1, unit_2):
    while True:
        unit_2.health -= unit_1.attack
        if (unit_2.health <= 0):
            unit_2.is_alive = False
            break
        unit_1.health -= unit_2.attack
        if (unit_1.health <= 0):
            unit_1.is_alive = False
            break
    if (unit_1.is_alive == True):
        return True
    return False


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False

    print("Coding complete? Let's try tests!")
