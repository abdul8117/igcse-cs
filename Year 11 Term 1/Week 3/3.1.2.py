# Psuedocode
"""

SET fruitCount = <input from user>
SET weights = []
SET sum_of_weights = 0

for loop:
  SET weight = <get weight of each fruit from the user>
  <append weight to weights>

for loop through the weights array:
  add i'th weight and sum_of_weight

print "<mean weight of the fruits>'

"""

fruitCount = int(input("Number of fruits: "))
weights = list()
sum_of_weights = 0

for i in range(0, fruitCount):
  weight = int(input(f"Weight {i + 1}: "))
  weights.append(weight)
  sum_of_weights += weights[i]

print(f"Mean weight: {round(sum_of_weights / len(weights), 2)}")