# average amount spent on food per week over 52 weeks. The amount per week is entered by the user.

spentOnFood = [ ]
weak = 1
Sum = 0

while weak <= 52:
  spentOnFoodInput = input("How much did you spend in weak" + str(weak) + "?")
  spentOnFood.append(spentOnFoodInput)
  weak = int(weak)
  weak = weak + 1

for i in spentOnFood: Sum = Sum + i


avg = spentOnFood / 52
print("Average spent per week:", avg)