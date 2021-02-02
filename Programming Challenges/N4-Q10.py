par3 = int(input("How many par 3 holes are there?\n"))
par4 = int(input("How many par 4 holes are there?\n"))
par5 = int(input("How many par 5 holes are there?\n"))

par3 = par3 * 3
par4 = par4 * 4
par5 = par5 * 5

difficulty = int(input("What is the difficulty adjustment for the course?\n"))

print(f"The Standard Scratch for the course is: {par3 + par4 + par5 + difficulty}")