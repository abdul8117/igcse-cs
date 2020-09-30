email = input("Enter your email address: ")
emailCheck = "@" in email

if emailCheck == True:
    print("Email is valid")
else:
    print("Email is invalid")