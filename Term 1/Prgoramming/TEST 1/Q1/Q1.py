rectangleOneLength =int(input("What is the length of the first rectangle? (only the value): "))
rectangleOneWidth =int(input("What is the width of the first rectangle? (only the value): "))

rectangleTwoLength = int(input("What is the length of the second rectangle? (only the value): "))
rectangleTwoWidth = int(input("What is the width of the second rectangle? (only the value): "))

rectangleOneArea = rectangleOneLength * rectangleOneWidth
rectangleTwoArea = rectangleTwoLength * rectangleTwoWidth

print("The area of rectangle one is:", rectangleOneArea)
print("The area of rectangle two is:", rectangleTwoArea)

if rectangleOneArea > rectangleTwoArea:
  print("Rectangle one is bigger than rectangle two")
else:
  print("Rectangle two is bigger than rectangle one")
