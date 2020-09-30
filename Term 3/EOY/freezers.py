freezers = [-20, -19, -18, -17, -16, 0, 1]

for temp in freezers:
  if temp == -18: print(f"Freezer number {freezers.index(temp) + 1} is the perfect temperature, -18C")
  elif temp < -18: print(f"Freezer number {freezers.index(temp) + 1} is too cold. It is {temp}C")
  else: print(f"Freezer number {freezers.index(temp) + 1} is too hot. It is {temp}C")