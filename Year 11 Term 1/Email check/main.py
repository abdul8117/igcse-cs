"""
save all text of emails.txt as a list

loop through the list of emails:
    check if it is valid through a regex:
        if not, ask the user to re-enter it and replace it on the list
        else, continue to the next email

after all emails have been checked:
    re-write the text file with the new, correct email list

custom functions: validate_email(email)
"""

# import re

# emails = list()

# def get_emails():
#     emails_file = open(r"emails.txt", "r")
#     emails = emails_file.readlines()
#     print(emails)



import re

emails = list()

def get_emails():
  # get email from the user
    while len(emails) < 5:
        email = input("Enter email: ")
        if validate_email(email):
            append_email(email)
    return True

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
    emails_file = open("emails.txt", "a")
    for email in emailList:
        emails_file.write(email)
    emails_file.close()
    
if get_emails():
    export_emails(emails)
    print(emails)