# input: weight, all dimensions

import math

# ask weight, all dimensions
weight = float(input("Weight: "))
length = float(input("Length: "))
width = float(input("Width: "))

if weight > 100 and length > 150 and width > 150:
    print("Should be sent by freight.")
    quit()

if weight < 10 and length < 40 and width < 30:
    print("No charge")
else:
    if weight < 20 and length < 60 and width < 40:
        print("$50")
    else:
        remainingWeight = weight - 20
        cost = remainingWeight * 10
        print(f"${cost}")