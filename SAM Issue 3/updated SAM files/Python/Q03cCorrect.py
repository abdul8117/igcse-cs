# Do not use any other data structure such as an array or a list.
count = 0               # A counter for the line numbers
theLine = ""            # Holds each line of the file

# Open "Cities.txt" as input
theFile = open ("Cities.txt", "r")

# Open "Numbered.txt" as output
outFile = open ("Numbered.txt", "w")

# Use a for/each loop to read each line of
# the input file into a variable named 'theLine'
for theLine in theFile:

    # Increment the line count
    count = count + 1

    # Add the line number to the front of the line followed by a space
    theLine = str(count) + " " + theLine

    # print the line to the display
    print (theLine)

    # Write the new line to the output file
    outFile.writelines (theLine)

# Close the input file
theFile.close()

# Close the output file
outFile.close()