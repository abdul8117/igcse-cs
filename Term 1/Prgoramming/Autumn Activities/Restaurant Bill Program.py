billAmount = int(input("What was your bill?"))
tipPercentage = int(input("How much tip would you like to give to the waiter (percentage)?"))
tipPercentage = tipPercentage / 100
tipAmount = billAmount * tipPercentage
print("You will pay this much in tips:", tipAmount)
totalBill = billAmount + tipAmount
print("Your total is:",totalBill)
