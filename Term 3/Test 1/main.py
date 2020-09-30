# variables
month = int(input("What month is it?\n"))
day = int(input("\nWhat day is it?\n"))

# main program
if month == 1:
  print("Do not open")
else:
  if month >= 5 and month <= 9:
    if day >= 1 and day <= 5:
      print("12:00 to 18:30")
    else:
      if day == 6 or day == 7:
        print("12:00 to 20:00")
      else:
        print("High season day error")
  else:
    if month >= 2 and month <= 12:
      if day >= 1 and day <= 5:
        print("13:00 to 17:00")
      else:
        if day == 6 or day == 7:
          print("13:00 to 18:00")
        else:
          print("Low season day error")
    else:
      print("Month error")