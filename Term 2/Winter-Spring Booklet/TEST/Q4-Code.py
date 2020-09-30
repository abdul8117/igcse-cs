userName = input("What is your name? ")
userEmail = input("What is your email? ")
userAge = int(input("What is your age? "))

      
# Validating user's name
while userName == "":
  if userName == "":
    print("Enter your name!")
    userName = input("What is your name? ")
  else:
    print("Name is valid")

# Validating user's email
emailCheck = "@gmail.com" in userEmail
if emailCheck == False:
  emailCheck = "@yahoo.com" in userEmail
else:
  print("Your email is valid")

while emailCheck == False:
  if emailCheck == True:
    print("Your email is valid.")
  else:
    print("Email was invalid")
    userEmail = input("What is your email? ")
    emailCheck = "@gmail.com" in userEmail
  if emailCheck == False:
    emailCheck = "@yahoo.com" in userEmail
  else:
    print("Your email is valid")

# Validating user's age 
userAgeCheck = False
while userAgeCheck == False:
  userAge = int(input("Confirm your age (1 - 80): "))
  if userAge <= 80 and userAge >= 1:
    userAgeCheck = True
  else:
    userAgeCheck = False
    print("Age is invalid")

print("Your name is:", userName)
print("Your email is:",  userEmail)
print("Your age is:", userAge)
