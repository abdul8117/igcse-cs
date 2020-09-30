statesOfMatter = ["Solid", "Liquid", "Gas"]
temperature = int(input("What is the temperature?: "))

if temperature <= 0:
  print(statesOfMatter[0])
elif temperature >= 100:
  print(statesOfMatter[2])
else:
  print(statesOfMatter[1])