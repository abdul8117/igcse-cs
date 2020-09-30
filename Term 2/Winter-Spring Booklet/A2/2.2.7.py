firstNum = int(input("Enter your first number: "))
secondNum = int(input("Enter your second number: "))

try:
  x = firstNum / secondNum
except: 
  print("You cannot divide by 0")
else:
  print(firstNum, "/", secondNum, "=", x)