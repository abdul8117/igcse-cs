ballCount = 1
over = [ ]
overTotal = 0

while ballCount <= 6:
  runs = int(input("Runs: "))
  over.append(runs)
  ballCount = ballCount + 1

for runs in over:
  overTotal = overTotal + runs
  print(runs)
print("Total runs:", overTotal)