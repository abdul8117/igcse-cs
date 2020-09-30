question = "How much money did you raise? (without currency symbol): "
friendOne = int(input(question))
friendTwo = int(input(question))
friendThree = int(input(question))

moneyRaised = friendOne + friendTwo + friendThree

if moneyRaised > 1000:
  print("The amount raised will be doubled by a local company.")
  print("The total money raised:", moneyRaised * 2)
else:
  print("The amount can't be doubled by the local company.")
  print("The total money raised:", moneyRaised)
