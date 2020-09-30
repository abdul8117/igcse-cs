"""
S - Number plate
    time arrived
    time leaving
    amount to be paid
    amount paid
I - what user pays
P - whether the full amount is paid
O - whether gate opens
    change



"""
numberPlate1 = int(input("Enter you number plate: "))
timeArrived = 1700
timeLeaving = 2100
timeSpent = timeLeaving - timeArrived
amountToBePaid = timeSpent * 3

numberPlate2 = int(input("Enter you number plate again: "))
if numberPlate1 == numberPlate2:
  print("The fee is:", amountToBePaid)
else:
  print("This car cannot leave the lot.")

print("The fee is:", amountToBePaid)

amountPaid = int(input("Enter how much you paid: "))
while amountPaid < amountToBePaid:
  if amountPaid < amountToBePaid:
    print("Pay more:", amountToBePaid - amountPaid)
    amountPaid = int(input("Enter how much you paid: "))