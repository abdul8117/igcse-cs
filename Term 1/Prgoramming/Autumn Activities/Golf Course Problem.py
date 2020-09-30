# number of shots
par3_shots = 0
par4_shots = 0
par5_shots = 0

par3_shots = 3
par4_shots = 4
par5_shots = 5

# initializing variables
par3_holes = 0
par4_holes = 0
par5_holes = 0
difficultyAdjustment = 0

# asking the player their results + error handling
try:
    par3_holes = int(input("How many par 3 holes are there? "))
except:
    print("Invalid inpuut")
try:
    par4_holes = int(input("How many par 4 holes are there? "))
except:
    print("Invalid inpuut")
try:
    par5_holes = int(input("How many par 5 holes are there? "))
except:
    print("Invalid inpuut")

if par3_holes or par4_holes or par5_holes < 0:
    print("You cannot enter negative numbers. Please restart the program.")
else:
    while difficultyAdjustment >= 0:
        try:
            difficultyAdjustment = int(input("What is the difficulty adjustment of the course (negative number)? "))
        except:
            print("Invlaid input")
            continue
        if difficultyAdjustment <= 0:
            print("Confirm your difficulty adjustment below.")
    try:
        difficultyAdjustmentConfirmation = int(input("What is the difficulty adjustment of the course (negative number)? "))
    except:
        print("Invalid input.")
    if difficultyAdjustment != difficultyAdjustmentConfirmation:
        print("The difficulty adjustment values were not the same. Please restart the program.")
    else:
        print("Here are your results:")
        par3_score = par3_holes * par3_shots # calculating the score of the player
        par4_score = par4_holes * par4_shots
        par5_score = par5_holes * par5_shots
        totalScore = par3_score + par4_score + par5_score
        finalScore = totalScore - difficultyAdjustment

        print(finalScore) # end if statement
