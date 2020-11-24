# input: weight, all dimensions

import math

# ask weight, all dimensions
w = float(input("Weight: "))
l = float(input("Length: "))
h = float(input("Height: "))

if w > 100 and l > 150 and h > 150:
    print("Should be sent by freight.")

if w < 10 and l < 40 and h < 30:
    print("No charge")
else:
    if w < 20 and l < 60 and h < 40:
        print("$50")
    else:
        remainingWeight = w - 20
        cost = remainingWeight * 10
        print(f"${cost}")