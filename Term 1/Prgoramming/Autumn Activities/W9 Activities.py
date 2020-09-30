"""
print((78 == 10) or (6 == 7))
print((78 == 10) or (6 == 6))
print((78 == 10) and (6 == 6))
print((1 < 10) and (2 < 10))
print((1 < 10) or (2 < 10))
print(not ( 5 == 5))
print(not (6 < 4))
"""

yearGroup = int(input("What year group are you in? "))

if (yearGroup == 1) or (yearGroup == 2):
    print("You are in Key Stage 1")
elif (yearGroup >= 3) and (yearGroup <= 6):
    print("You are in Key Stage 2")
elif (yearGroup >=7) and (yearGroup <=9):
    print("You are in Key Stage 3")
elif (yearGroup == 10) or (yearGroup == 11):
    print("You are in Key Stage 4")
else:
    print("Your year group is not part of the Key Stage organisation.")
