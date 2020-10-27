"""
a = [[1, 2, 3], [4, 5, 6]]
print(a[0])
print(a[1])

b = a[0]
print(b)
print(a[0][2])

a[0][1] = 7
print(a)
print(b)

b[2] = 9
print(a[0])
print(b)
"""

# Activity 1.2.3

numbRows = 9
numbCols = 5
myArray=[[0 for column in range(numbCols)] for row in range(numbRows)]
print(myArray)

myArray[0][4] = 99
myArray[2][3] = 74
print(myArray)

# print out a row at a time
for row in range(numbRows):
    print(myArray[row])
