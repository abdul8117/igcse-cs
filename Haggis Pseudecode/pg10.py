from random import randint

chosenNumber = randint(1,21)
userNumber = 0
count = 0
print("I am thinking of a whole number between 1 and 20")

while userNumber != chosenNumber:
  try:
    userNumber = int(input("Guess a number: "))
  except:
    print("Invalid.")
    continue

  if userNumber == chosenNumber:
    print("Correct. I was thinking of", chosenNumber)

  if userNumber < 1 or userNumber > 20:
    print("Enter a whole number between 1 and 20.")
    userNumber = int(input("Guess a number: "))
    continue

  count = count + 1

  if userNumber < chosenNumber:
    print("My number is bigger than your guess.")
  if userNumber > chosenNumber:
    print("My number is smaller than yours.")

print("Number of valid guesses: ", count)
