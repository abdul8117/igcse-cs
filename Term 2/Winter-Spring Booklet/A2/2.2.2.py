password = input("Password: ")
lengthCheck = len(password)

if lengthCheck >= 8:
    print("Access Granted")
else:
    print("Your password should be atleast 8 characters long")
