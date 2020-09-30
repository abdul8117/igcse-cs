uknownNum = 45
userGuess = int(input("Guess a number between 1-100: "))

if userGuess == 45:
  print("Correct!")

while userGuess != uknownNum:
  if userGuess > uknownNum:
    print("Too high")
    userGuess = int(input("Guess a number between 1-100: "))
  elif userGuess < uknownNum:
    print("Too low")
    userGuess = int(input("Guess a number between 1-100: "))

if userGuess == 45:
  print("Correct!")