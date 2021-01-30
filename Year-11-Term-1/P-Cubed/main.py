# get input from the user
# validate input (> 0)
# append to a list
# count the number of items
# output heaviest, lightest item

weights = []  

def get_input():
    weight = 1
    while weight > 0:
        weight = int(input("Enter the weight of the item. 0 to quit.\n"))

        if weight < 0:
            print("Error. No negatives allowed.")
            weight = 1
        elif weight == 0:
            break
        else:
            weights.append(weight)

def main():
    get_input()

    if len(weights) == 0:
        print("No items")
        quit()

    print(f"\nNumber of items: {len(weights)} \nHeaviest item: {max(weights)} \nLightest item: {min(weights)}")

main()