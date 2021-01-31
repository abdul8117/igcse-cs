# record 10 products
# product code, name, quantity, and price about the products
# ask the customer to enter the product code for the things they are buying
# calculate total price
# if more than 3 products, 10% disc, if > 5, 20% disc
# update stock if item is sold
# produce a list of stock with quantity < 5
# add new products to stock
# update quantity of existing products



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


def calc_total(products):
    cost = 0
    i = 0

    for i in stock:
        if stock[i][0] == products[i]:
            cost += stock[i][-1]
        i += 1
    
    return cost


def main():
    record_products(3)


    # ask customer for product code(s)
    num_of_products_bought = int(input("How many products do you have? "))
    product_codes = []

    for i in range(num_of_products_bought - 1):
        code = input("Product code: ")
        product_codes.append(code)

    # calculate total price
    total = calc_total(product_codes)

    print(total)


main()
