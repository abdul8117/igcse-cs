"""
num1 = 0
num2 = 0
num3 = 0

num1 = int(input("Number 1: "))
num2 = int(input("Number 2: "))
num3 = int(input("Number 3: "))

total = num1 + num2 + num3
print("The total is:", total)
"""

# a random number is given by the randint() function
import random
answer = random.randint(1,6)
if answer == 1:
	print("You will make a new friend this week")
elif answer == 2:
	print("You will do well in your GCSEs")
elif answer == 3:
	print("You will find something you thought you’d lost")
elif answer == 4:
    print("A dog will infect you with rabies")
elif answer == 5:
    print("Your will find insects in your sink next week")
elif answer == 6:
    print("A brick will fall on you next year")

