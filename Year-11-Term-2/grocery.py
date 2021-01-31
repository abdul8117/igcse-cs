# record 10 products
# product code, name, quantity, and price about the products

# ask the customer to enter the product code for the things they are buying
# calculate total price
# if more than 3 products, 10% disc, if > 5, 20% disc

# update stock if item is sold
# produce a list of stock with quantity < 5
# update quantity of existing products

# add new products to stock


# record 10 products
stock = []

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


def low_stock(stock_):
    # produce a list of stock with quantity < 5
    low_stock = []

    for product in stock_:
        if product[2] < 5:
            low_stock.append(product)

    return low_stock


def add_new(code, name, quantity, price):
    item = [code, name, quantity, price]
    stock.append(item)


def main():
    record_products(2)

    # ask customer for product code(s)
    num_of_products_bought = int(input("How many products do you have? "))
    product_codes = []

    for i in range(num_of_products_bought):
        code = input("Product code: ")
        product_codes.append(code)

    # calculate total price
    total_cost = 0
    for i in range(len(product_codes)):
        for j in stock:
            if product_codes[i] == j[0]:
                total_cost += j[-1]
    
    print(total_cost)

    # apply discount
    # if more than 3 products, 10% disc, if > 5, 20% disc
    if 3 > num_of_products_bought >= 5:
        total_cost *= 0.8
    elif num_of_products_bought > 5:
        total_cost *= 0.9


    low_in_stock = low_stock(stock)
    print("\nLow in stock (<5):")
    for i in low_in_stock: print(i)

    # ask user to update stock quantity
    index = 0
    for i in low_in_stock:
        if i in stock:
            num_to_add = int(input(f"Quantity to add to {i[1], i[0]}: "))
            stock[index][2] += num_to_add
        index += 1


    # add new products to stock
    while True:
        add = input("Add new product? (y/n) ")
        if add.lower() == "n":
            break

        p_code = input(f"Product code: ")
        p_name = input(f"Product name: ")
        p_quantity = int(input(f"Product quantity: ")) 
        p_price = float(input(f"Product price: "))

        add_new(p_code, p_name, p_quantity, p_price)
    
    
    print("Current stock:")
    for i in stock:
        print(i)


main()
