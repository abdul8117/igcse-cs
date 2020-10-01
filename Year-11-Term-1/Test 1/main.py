def get_subjects():

  # get the two subjects from the user
  subject_1 = input("Subject 1: ").lower()
  subject_2 = input("Subject 2: ").lower()

  department(subject_1, subject_2)

def department(subject1, subject2):

  # engineering
  if (subject1 == "maths" and subject2 == "physics") or (subject1 == "physics" and subject2 == "maths"):
    print("Your department is Engineering.") 
  # medicine
  elif (subject1 == "chemistry" and subject2 == "biology") or (subject1 == "biology" and subject2 == "chemistry"):
    print("Your department is Medicine.")
  # law
  elif (subject1 == "politics" and subject2 == "english") or (subject1 == "english" and subject2 == "politics"):
    print("Your department is Law.")
  # computer science
  elif (subject1 == "computing" and subject2 == "ict") or (subject1 == "ict" and subject2 == "computing"):
    print("Your department is Computer Science")
  # no departments
  else:
    print("Departments do not match.")

get_subjects()