weight = int(input("Weight: "))
length = int(input("Length:"))
width = int(input("Width: "))
# depth = int(input("Depth: "))

charge = 0

if weight > 100 and length > 150 and width > 150:
    print("Use freight.")
    charge = -99
    quit()

if weight < 10 and length < 40 and width < 30:
    print("Free.")
elif weight < 20 and length < 60 and width < 40:
    charge = 50
else:
    charge = weight * 10 + 50

print(f"Charge: ${charge}")
