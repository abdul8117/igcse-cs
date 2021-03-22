# User enters a logical expression
# for examples, A . B + C

# Create a table of all possible outputs 

# Handle AND, OR, NOT
# AND: .  ^  &
# OR: v  +  ||
# NOT: !  ~  ¬

# .  +  !





def AND(a, b):
    if  a == b:
        return 1
    elif a != b:
        return 0


def OR(a, b):
    if a == 1:
        return 1
    elif b == 1:
        return 1
    else:
        return 0


def NOT(a):
    if a == 1:
        return 0
    elif a == 0:
        return 1


def main():
    exp = input("Logical expression: ")

    # create a list of the different letters
    # 
    # iterate through the input
    # if char is a symbol, then evaluate the expression using the left and right chars
    



main()