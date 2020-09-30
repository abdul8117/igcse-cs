"""
Line 1 REPEAT
Line 2 RECEIVE usersPassword FROM (STRING) KEYBOARD
Line 3 RECEIVE usersPassword2 FROM (STRING) KEYBOARD
Line 4 IF usersPassword <> usersPassword2 THEN SEND <Error_Message> TO DISPLAY
Line 5 UNTIL usersPassword = usersPassword2
"""
userPassword = ""
userPasswordCheck = None

while userPassword != userPasswordCheck:
  userPassword = input("Enter password: ")
  userPasswordCheck = input("Confirm password: ")
  if userPassword != userPasswordCheck:
    print("Passwords should be the same")
