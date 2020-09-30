import winsound

uInput = int(input("Enter a number between 1 and 10: "))

if uInput == 1:
  winsound.Beep(100, 1500)
elif uInput == 3:
    winsound.Beep(200, 1500)
elif uInput == 4:
    winsound.Beep(400, 1500)
elif uInput == 5:
    winsound.Beep(800, 1500)
elif uInput == 6:
    winsound.Beep(1000, 1500)
elif uInput == 7:
    winsound.Beep(1500, 1500)
elif uInput == 8:
    winsound.Beep(2450, 1500)
elif uInput == 9:
    winsound.Beep(5000, 1500)
elif uInput == 10:
    winsound.Beep(12500, 1500)