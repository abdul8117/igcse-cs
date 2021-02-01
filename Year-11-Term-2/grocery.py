# record 10 products
# product code, name, quantity, and price about the products

# ask the customer to enter the product code for the things they are buying
# calculate total price
# if more than 3 products, 10% disc, if > 5, 20% disc

# update stock if item is sold
# produce a list of stock with quantity < 5
# update quantity of existing products

# add new products to stock


stock = []

# record products
def record_products(n):
    count = 1

    for i in range(n):
        product_details = []

        p_code = input(f"Product code {count}: ")
        p_name = input(f"Product name {count}: ")
        p_quantity = int(input(f"Product quantity {count}: ")) 
        p_price = float(input(f"Product price {count}: "))
        print("\n")

        product_details.append(p_code)
        product_details.append(p_name)
        product_details.append(p_quantity)
        product_details.append(p_price)

        stock.append(product_details)
        count += 1


def print_low_in_stock(stock_):
    # produce a list of stock with quantity < 5
    global low_stock
    low_stock = []

    for product in stock_:
        if product[2] < 5:
            low_stock.append(product)

    print("Products low in stock (<5):")
    for i in low_stock:
        print(f"{i[1]}, {i[2]} left.")


def add_new(code, name, quantity, price):
    item = [code, name, quantity, price]
    stock.append(item)


def main():
    record_products(2)

    print(*stock, sep="\n")

    # ask customer for product code(s)
    product_codes = []
    num_of_products = 0

    print("\n\nWhat have you bought?")
    while True:
        code = input("Product code: ")

        if code == "":
            break

        product_codes.append(code)
        num_of_products += 1

    # calculate total price
    total_cost = 0
    for i in range(len(product_codes)):
        for j in stock:
            if product_codes[i] == j[0]:
                total_cost += j[-1]
    
    print(f"\nTotal cost: {total_cost}")

    # decrease stock for products bought
    for i in range(len(stock)):
        for j in product_codes:
            if j in stock[i][0]:
                stock[i][2] -= 1

    # apply discount
    # if more than 3 products, 10% disc, if > 5, 20% disc
    if 3 > num_of_products >= 5:
        total_cost *= 0.8
    elif num_of_products > 5:
        total_cost *= 0.9


    # print products low in stock, <5
    print_low_in_stock(stock)

    # ask user to update stock quantity
    index = 0
    for i in low_stock:
        if i in stock:
            num_to_add = int(input(f"\nQuantity to add to {i[1], i[0]}: "))
            stock[index][2] += num_to_add
        index += 1


    # add new products to stock
    while True:
        add = input("\nAdd new product? (y/n) ")
        if add.lower() == "n":
            break

        p_code = input(f"Product code: ")
        p_name = input(f"Product name: ")
        p_quantity = int(input(f"Product quantity: ")) 
        p_price = float(input(f"Product price: "))

        stock.append([p_code, p_name, p_quantity, p_price])
    
    
    print("\nCurrent stock:")
    print(*stock, sep="\n")


main()
