userName = input("What is your name? ")
userEmail = input("What is your email? ")
userAge = int(input("What is your age? "))

# Validating user's name
if userName == "":
    print("Enter your name!")
    userName = input("What is your name? ")
else:
    print("Name is valid")

# Validating user's email
emailCheck = "@" in userEmail
if emailCheck == True:
    print("Email is valid")
else:
    print("Email is invalid")

# Validating user's age 
for num in userAge:
  