def AND(a, b):
    """
    a  -  b
    0  -  0  - 0
    1  -  0  - 0
    0  -  1  - 0
    1  -  1  - 1
    """

    if  a == b:
        return 1
    elif a != b:
        return 0


def OR(a, b):
    """
    a  -  b
    0  -  0  -  0
    1  -  0  -  1
    0  -  1  -  1
    1  -  1  -  1
    """

    if a == 1:
        return 1
    elif b == 1:
        return 1
    else:
        return 0


def NOT(a):
    """
    a
    0  -  1
    1  -  0
    """

    if a == 1:
        return 0
    elif a == 0:
        return 1


def main():

    x = int(input("A: "))
    y = int(input("B: "))

    print("\nAND:", AND(x, y))
    print("OR:", OR(x, y)) 


main()