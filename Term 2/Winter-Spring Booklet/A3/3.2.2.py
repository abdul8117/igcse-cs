def function_one(myName):
	print("Hello",myName)
function_one("Norman")

def name_age(name = "Norman", age = 16):
    print("My name is", name, "and I am", age)

name_age()
name_age("John", 19)
name_age("Jamie", 17)

def squareArea(length = 0):
    area = length**2
    print(area)

squareArea(3)
squareArea(9)
squareArea(16)
