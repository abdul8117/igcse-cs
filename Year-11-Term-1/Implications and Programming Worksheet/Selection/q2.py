products = ["water (1)", "crisps (2)", "chocolate bar (3)"]
prices = [1, 0.5, 0.65]

print(products, "\n Prices: ", prices)

request = int(input("Choose: "))
money = float(input("Coins: "))

index = request - 1

if prices[index] > money:
    print("Insufficient coins")
else:
    print(f"Change: {round(money - prices[index], 2)}")