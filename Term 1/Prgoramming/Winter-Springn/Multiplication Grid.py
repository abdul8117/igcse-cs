# Write a program that fills up a two-dimensional grid with the results of
# the multiplication table 10 x 10 and prints out the result.

numbRows = 10
numbCols = 10
table = [[0 for column in range(numbCols)] for row in range(numbRows)]

for row in range(1,10):
    for column in range(1,10):
        table[row][column] = row*row

print(table)
