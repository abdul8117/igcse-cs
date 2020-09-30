studentName = str(input("What is your Name?"))
mathMark = int(input("Math marks: "))
biologyMark = int(input("Biology marks: "))
chemistryMark = int(input("Chemistry marks: "))
physicsMark = int(input("Physics marks: "))
geographyMark = int(input("Geography marks: "))

totalMark = mathMark + biologyMark + chemistryMark + physicsMark + geographyMark
avgMark = totalMark / 5

if avgMark > 90:
  print("Grade A")
elif avgMark > 80:
  print("Grade B")
elif avgMark > 70:
  print("Grade C")
elif avgMark > 60:
  print("Grade D")
else:
  print("Grade E")