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

nameList = []
ageList = []
emailList = []
counter = 0

def get_name():
  for i in range(5):
    name = input(f"Name {i+1}: ")
    while validate_name(name) == False:
      print("Invalid name")
      counter -= 1
      break
    nameList.append(name)

def validate_name(name):
  if name == "":
    return False
  else:
    return True

def get_age():
  for i in range(5):
    age = int(input(f"Age {i+1}: "))
    while validate_age(age) == False:
      print("Invalid age")
      i -= 1
      break
    ageList.append(age)

def validate_age(age):
  if age < 8 or age > 80:
    return False
  else:
    return True


def get_email():
  for i in range(5):
    email = input(f"Email {i+1}: ")
    while validate_email(email) == False:
      print("Invalid email")
      i -= 1
      break
    emailList.append(email)

def validate_email(email):
  if "@" in email:
    return True
  else:
    return False

def main():
  get_name()
  get_age()
  get_email()
  print(nameList, ageList, emailList)

main()