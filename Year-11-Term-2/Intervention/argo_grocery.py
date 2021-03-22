# Question 5: Agro company sells food products. 
# Write a program which will store product id, name and price of food item. 
# Print the average and total price of all the items. 
# Display the three most expensive items. 
# Ask user to enter the details of a new item to the list and display all food items.

# Sample data: ID, Name, Price
# Food=[[101, “ Potato”, 12] , [102, “ Tomato”, 15], [103, “ Apple”, 4], [104, “ Rice”, 8], [105, “ Wheat”, 22], [106, “ Oil”, 18] ,[107, “ Milk”, 4]]

food = [[101, "Potato", 12], [102, "Tomato", 15], [103, "Apple", 4], [104, "Rice", 8], [105, "Wheat", 22], [106, "Oil", 18], [107, "Milk", 4]]

print(*food, sep="\n")


# print total, average
total = 0

for item in food:
    total += item[2]

average = total / len(food)

print("Total cost:", total)
print("Average cost:", average)


# 3 most expensive

def 
