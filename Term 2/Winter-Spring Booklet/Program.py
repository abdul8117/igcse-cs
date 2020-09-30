userNum = int(input("Enter a number between 1 and 50: "))

while userNum < 1 or userNum > 50:
  print("Number is too high or too low")
  userNum = int(input("Enter a number between 1 and 50: "))

while userNum >= 1 and userNum <= 50:
  userNumSquare = userNum**2
  userNumCube = userNum**3
  print("The square of your number is:", userNumSquare)
  print("The cube of your number is:", userNumCube)
  break
