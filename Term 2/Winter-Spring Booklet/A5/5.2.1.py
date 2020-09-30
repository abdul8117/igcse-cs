from decimal import Decimal

products = ["Dog food 5kg [1]", "Cat food [2]", "Water [3]", "Apple [4]", "Mango [5]"]
PRICING = [0, 31, 11, 2, 5, 13]
VAT = 1.2
invoice = 0
userKart = 0

print(products)
while userKart != "done":
  userKart = input("What would you like to buy?")
  if userKart == "1":
    invoice = PRICING[1]
  elif userKart == "2":
    invoice = PRICING[2]
  elif userKart == "3":
    invoice = PRICING[3]
  elif userKart == "4":
    invoice = PRICING[4]
  elif userKart == "5":
    invoice = PRICING[5]
  

def applyDiscount():
  global invoice
  if invoice < 10:
    invoice = invoice * (1 - 0.05)
  elif invoice < 30:
    invoice = invoice * (1 - 0.10)
  elif invoice >= 30:
    invoice = invoice * (1 - 0.15)

def applyVAT():
  global finalInvoice 
  finalInvoice = 0
  finalInvoice = invoice * VAT

applyDiscount()
applyVAT()

print("Your need to pay:", round(finalInvoice, 3))
