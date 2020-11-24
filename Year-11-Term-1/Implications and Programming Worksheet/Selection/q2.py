products = ["water", "crisps", "chocolate bar"]
prices = [1, 0.5, 0.65]

print(products, prices)

req = input("Choose: ")
money = float(input("Coins: "))

index = products.index(req.lower())

if prices[index] > money:
    print("insufficient coins")