# User enters a logical expression
# for examples, A . B + C

# Create a table of all possible outputs 

# Handle AND, OR, NOT
# AND: .  ^  &
# OR: v  +  ||
# NOT: !  ~  ¬

# .  +  !


def AND(a, b):
    if  a == 1 and b == 1:
        return 1
    else:
        return 0
    

def OR(a, b):
    if a == 1:
        return 1
    elif b == 1:
        return 1
    else:
        return 0


def NOT(a):
    if a == 0:
        return 1
    elif a == 1:
        return 0



# create a list of the different letters 
# iterate through the input
# if char is a symbol, then evaluate the expression using the left and right chars


# def parse(exp, a, b):
#     for char in exp:



A = [0, 1]
B = [0, 1]
# A = [1]
# B = [0]
# C = [0, 1]

AND_SYMBOLS = ["."]
OR_SYMBOLS = ["+"]
NOT_SYMBOLS = ["!"]

# expression = input("Logical expression: ")
expression = "A.B"

answer = []


# for i in A:
#     for j in B:
#         x = AND(i, j)
#         answer.append(x)

for i in A:
    for j in B:
        for char in expression:
            if char == ".":
                x = AND(i, j)
            elif char == "+":
                x = OR(i, j)

print(answer)