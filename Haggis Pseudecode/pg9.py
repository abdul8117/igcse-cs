itemsBoughtCost = 0
itemsCost = [ ]
typeOfCustomer = " "
totalCost = 0
finalCost = 0
counter = 1

while itemsBoughtCost != "done":
  itemsBoughtCost = input("Price of item " + str(counter) + ": ")
  if itemsBoughtCost != "done":
    itemsBoughtCost = int(itemsBoughtCost)
    itemsCost.append(itemsBoughtCost)
    counter = int(counter)
    counter = counter + 1
    continue
  break

for i in itemsCost: totalCost = totalCost + i
vatTotal = 0.175 * totalCost

while typeOfCustomer != "P" or typeOfCustomer != "S":
  typeOfCustomer = input("Type of Customer: ")
  if typeOfCustomer != "P" or typeOfCustomer != "S":
    print("Please enter P or S")
  break

if typeOfCustomer == "S": finalCost = totalCost
else: finalCost = totalCost + vatTotal

print("Total cost of purchases:", totalCost)
print("Type of customer:", typeOfCustomer)
print("VAT:", vatTotal)
print("Final Cost:", finalCost)
