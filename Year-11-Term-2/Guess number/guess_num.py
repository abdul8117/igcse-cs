import random

f = open("Year-11-Term-2/Guess number/log.txt", "a")

num = random.randint(0, 100+1)
f.write(f"Random number is {num}\n")

correct = False
tries = 0

while correct == False:
    guess = int(input("Guess a number between 1 and 100: "))

    if guess > num:
        print("Too high.")
        f.write(f"{tries}: Guess ({guess}) is too high.\n")
    elif guess < num:
        print("Too low.")
        f.write(f"{tries}: Guess ({guess}) is too low.\n")
    else:
        print("Correct.")
        f.write(f"{tries}: Guess ({guess}) is correct.\n")
        correct = True
        tries += 1
    
    tries += 1

print("Tries", tries)