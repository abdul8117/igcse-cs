binary = input("Enter a binary number: ")
denary = 0

for digit in binary:
    denary = int(digit) + denary * 2 

print("Your denary number is: " + str(denary))
