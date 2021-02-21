import math

data_set = [3, 9, 13, 15, 21, 24, 27, 30, 36, 39, 42, 54, 69]
first = 0
last = len(data_set) - 1
found = False
target = int(input("Number to search: "))

while found == False and first <= last:
    middle = math.ceil((first + last) / 2)

    if data_set[middle] == target:
        found = True
        print(f"{target} is found.")
    
    elif target > data_set[middle]:
        first = middle - 1
    
    elif target < data_set[middle]:
        last = middle + 1
    
if found == False:
    print("Not found.")

