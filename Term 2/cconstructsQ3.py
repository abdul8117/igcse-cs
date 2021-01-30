stock = {
  "apple": 5, 
  "banana": 6, 
  "bread": 13, 
  "chocolate": 0
}

for product, quantity in stock.items():
  print(product, quantity)
  if quantity == 0:
    print(product, "is out of stock.")
