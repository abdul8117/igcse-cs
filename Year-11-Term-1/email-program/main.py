import re

emails = list()

def get_emails():
  # get email from the user
    while len(emails) < 5:
        email = input("Enter email: ")
        if validate_email(email):
            emails.append(email)
    return True

def validate_email(emailToValidate):
    regex = r"^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"

    if (re.search(regex, emailToValidate)):
        return True
    else:
        print(f"Incorrect email: {emailToValidate}")
        return False

def export_emails(emailList):
    emails_file = open(r"Year-11-Term-1/email-program/emails.txt", "a")
    for email in emailList:
        emails_file.write(f"{email}\n")
    emails_file.close()

if get_emails():
    export_emails(emails)