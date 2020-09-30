batteryPercent = int(input("How much percent of charge is left on your phone?"))

if batteryPercent <= 100 and batteryPercent >= 0:
  batteryCheck = True
  print("Value is valid")
else:
  batteryCheck = False
  print("Value is invalid")

while batteryCheck == False:
  batteryPercent = int(input("How much percent of charge is left on your phone?"))
  
  if batteryPercent <= 100 and batteryPercent >= 0:
    batteryCheck = True
    print("Value is valid")
  else:
    batteryCheck = False
    print("Value is invalid")
