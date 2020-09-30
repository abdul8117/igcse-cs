count = 1
productList = [ ]
priceList = [ ]

while count <= 5:
  count = count + 1
  product = input("Item: ")
  productList.append(product)
  price = input("price: ")
  priceList.append(price)

count = 1
while count <= 5:
  for item in productList:
    for price in priceList:
      print(item, "$", price)
  count = count + 1