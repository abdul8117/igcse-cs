import string


def increment_index(key, index):
    if key > 0:
        for i in range(key):
            if index == 25:
                index = 0
                    
            index += 1
            
    if key < 0:
        for i in range(abs(key)):
            if index == 0:
                index = 25

            index += 1
    
    return index


def shift(string_, key):
    alphabet_l = list(string.ascii_lowercase)
    alphabet_h = list(string.ascii_uppercase)
    output = ""

    if key == 0:
        return output

    for i in string_:

        if (i not in alphabet_l) and (i not in alphabet_h):
            output += i
            continue
        
        elif ord(i) < 97:
            # uppercase
            index = increment_index(key, alphabet_h.index(i))

            output += alphabet_h[index]

        else:
            # lowercase
            index = increment_index(key, alphabet_l.index(i))

            output += alphabet_l[index]
            

    return output


def main():
    phrase = input("Type phrase:\n")
    key = int(input("Key:\n"))

    print(shift(phrase, key))


main()