# outputs a number
def display(number, answer, type):
    print("This number {0} has been {2} the answer is {1}".format(number, answer, type))

# squares a number
def square(number):
    answer = number * number
    return(answer)

# main program
amount = int(input("Please enter number: "))
for next in range(1, amount):
    ans = square(next)
    display(next, ans,"squared")
