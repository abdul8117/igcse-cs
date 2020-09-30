def main(number):

    anArray = []
    f = False
    c = -1
    i = 0
    b = 75

    if isinstance(number, int):
        anArray.append(number)

    while (f == False):
        if anArray[i] == b:
            f = True
            c = i
        else:
            i += 1

    return c

main([2, 12, 3, 3])