"""
numbRows = 4
numbCols = 6
myArray=[[0 for column in range(numbCols)] for row in range(numbRows)]
print(myArray)
"""

"""
numbRows = 4
numbCols = 6
myArray=[[86 for column in range(numbCols)] for row in range(numbRows)]
print(myArray)
"""

"""
numbRows = 9
numbCols = 5
myArray=[[0 for column in range(numbCols)] for row in range(numbRows)]
#print(myArray)

myArray[0][4] = 99
myArray[2][3] = 74
#print(myArray)

for row in range(numbRows):
    print(myArray[row])
"""

#Write a program that fills up a two-dimensional grid
#with the results of the multiplication table 10 x 10 and
#prints out the result.



numbRows = 10
numbCols = 10

table = [[0 for column in range(numbCols)] for row in range(numbRows)]
for row in range(numbRows):
    print(table[row])

table[0][0] = 1
table[1][0] = 2
table[2][0] = 3
table[3][0] = 4
table[4][0] = 5
table[5][0] = 6
table[6][0] = 7
table[7][0] = 8
table[8][0] = 9
table[9][0] = 10

for row in range(numbRows):
    print(table[row])


for column in range(1,10):
    for row in range(1,10):
        table[column][row] = 

print(table)
