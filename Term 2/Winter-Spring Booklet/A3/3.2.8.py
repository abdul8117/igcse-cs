# outputs a number
def display(number, answer, type, answerC, typeC):
  print("This number {0} has been {2} the answer is {1}".format(number, answer, type))
  print("This number {0} has been {2} the answer is {1}".format(number, answerC, typeC))

# squares a number          
def square(number):
  answer = number * number
  return(answer)

answer=0
# cubes a number
def cube(number):
  answerC = number ** 3
  return(answerC)

# main program
amount = int(input("Please enter number: "))
for next in range(1, amount):
  ans = square(next)
  ansC = cube(next)
  display(next, ans,"squared", ansC, "cubed")
