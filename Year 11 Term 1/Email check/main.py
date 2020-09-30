"""
ask user for 5 emails
insert the emails into a text file, separated by a semi colon


for every email, check if it is valid
"""


































import re

emails = list()

def get_emails():
  # get email from the user
  while len(emails) < 5:
    email = input("Enter email: ")
    if validate_email(email):
      append_email(email)

def validate_email(emailToValidate):
    regex = r"^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"

    if (re.search(regex, emailToValidate)):
      return True
    else:
        print(f"Incorrect email: {emailToValidate}")
        return False

def append_email(emailToAppend):
  emails.append(emailToAppend)

def export_emails(emailList):
  file = open("emails.txt", "w")
  for email in emailList:
    file.write(email)

  file.close()
    
get_emails()