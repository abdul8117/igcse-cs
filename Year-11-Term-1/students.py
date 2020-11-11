# get name
# validate name
# add to list

# get age
# validate age
# add to list

# get email
# validate email
# add to list

# display list

import re

nameList = []
ageList = []
emailList = []
NUMBER_OF_STUDENTS = int(input("Number of students: "))

def get_name():
  i = 0

  while i < NUMBER_OF_STUDENTS:
    name = input(f"Name {i+1}: ")

    if validate_name(name) == False:
      print("Invalid name")
    else:
      i += 1
      nameList.append(name)

def validate_name(name):
  if name.strip() == "":
    return False
  else:
    return True

def get_age():
  i = 0

  while i < NUMBER_OF_STUDENTS:
    age = input(f"Age {i+1}: ")

    if validate_age(age):
      i += 1
      ageList.append(age)
    else:
      print("Invalid age")

def validate_age(age):
  if age.isnumeric():
    if (8 < int(age) < 80):
      return True
    else:
      return False
  else:
    return False

def get_email():
  i = 0

  while i < NUMBER_OF_STUDENTS:
    email = input(f"Email {i+1}: ")

    if validate_email(email):
      i += 1x
      emailList.append(email)
    else:
      print("Invalid email")
      

def validate_email(email):
  regex = r"^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
  
  if re.search(regex, email):
    return True
  else:
    return False

def main():
  get_name()
  get_age()
  get_email()
  print(nameList, '\n', ageList, '\n', emailList)

main()