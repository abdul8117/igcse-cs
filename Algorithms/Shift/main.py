# implement a shift cipher
# ask for a word and cipher key

import string

def shift(string_, key):
    alphabet_l = list(string.ascii_lowercase)
    alphabet_h = list(string.ascii_uppercase)
    output = ""

    for i in string_:
        
        if (i not in alphabet_l) and (i not in alphabet_h):
            output += i
            continue 

        if ord(i) < 97:
            # uppercase
            index = alphabet_h.index(i)
            # if i is A, index = 0

            if index >= 26:
                index = index - 25
                return alphabet_h[index]
            
            output += alphabet_h[index+key]

        else:
            # lowercase
            index = alphabet_l.index(i)

            if index >= 26:
                index = index - 25
                return alphabet_l[index]
            
            output += alphabet_l[index+key]
        
    return output


def main():
    phrase = input("Type phrase:\n")
    key = int(input("Key:\n"))

    print(shift(phrase, key))


main()