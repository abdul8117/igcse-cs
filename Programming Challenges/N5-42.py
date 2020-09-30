dancer1_name = input("Please enter a name:\n")
dancer1_age = int(input("Age:\n"))
dancer1_level = ""

dancer2_name = input("Please enter a name:\n")
dancer2_age = int(input("Age:\n"))
dancer2_level = ""

dancer3_name = input("Please enter a name:\n")
dancer3_age = int(input("Age:\n"))
dancer3_level = ""

dancer4_name = input("Please enter a name:\n")
dancer4_age = int(input("Age:\n"))
dancer4_level = ""

if dancer1_age >= 18: dancer1_level = "Senior"
elif dancer1_age < 12: dancer1_level = "Junior"
else: dancer1_level = "Teen"

if dancer2_age >= 18: dancer2_level = "Senior"
elif dancer2_age < 12: dancer2_level = "Junior"
else: dancer2_level = "Teen"

if dancer3_age >= 18: dancer3_level = "Senior"
elif dancer3_age < 12: dancer3_level = "Junior"
else: dancer3_level = "Teen"

if dancer4_age >= 18: dancer4_level = "Senior"
elif dancer4_age < 12: dancer4_level = "Junior"
else: dancer4_level = "Teen"

print("Names and competition list:")
print(dancer1_name + " - " + dancer1_level)
print(dancer2_name + " - " + dancer2_level)
print(dancer3_name + " - " + dancer3_level)
print(dancer4_name + " - " + dancer4_level)