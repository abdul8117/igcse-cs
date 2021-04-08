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
C = [0, 1]

# AND_SYMBOLS = ["."]
# OR_SYMBOLS = ["+"]
# NOT_SYMBOLS = ["!"]


expression = input("Logical expression:\n")
answer = []

for i in A:
    for j in B:
        for k in C:

            # first check for nots
            if "!" in expression:
                for l in range(len(expression) - 1):
                    if l == "!":
                        if expression[l + 1] == "A":
                            i = NOT(i)
                        elif expression[l + 1] == "B":
                            j = NOT(j)
                        elif expression[l + 1] == "C":
                            k = NOT(k)
 

            for char in expression:

                if char == "." or char == "+":

                    if char == ".":
                        x = AND(i, j)
                    
                    elif char == "+":
                        x = OR(i, j)
                    
                    for m in range(len(expression) - 1):
                        if expression[m + 1] == "C" or expression[m + 2] == "C":
                            if expression[m] == ".":
                                x = AND(x, k)
                                answer.append(x)
                            elif expression[m] == "+":
                                x = OR(x, k)
                                answer.append(x)



                # if char == ".":
                #     x = AND(i, j)

                #     for m in range(len(expression) - 1):
                #         if expression[m] == ".":
                #             if expression[m + 1] == "C" or expression[m + 2] == "C":
                #                 x = AND(x, k)
                #                 answer.append(x)

                # elif char == "+":
                #     x = OR(i, j)

                #     for n in range(len(expression) - 1):
                #         if expression[n] == "+":
                #             if expression[n + 1] == "C" or expression[n + 2] == "C":
                #                 x = OR(x, k)
                #                 answer.append(x)

                

print(answer)