# Do not use any other data structure such as an array or a list.
count = 0               # A counter for the line numbers
theLine = ""            # Holds each line of the file

# Open "Cities.txt" as input
f_cities = open("SAM Issue 3/updated SAM files/Python/Cities.txt", "r")

# Open "Numbered.txt" as output
f_cities_numbered = open("SAM Issue 3/updated SAM files/Python/Numbered.txt", "w")

# Use a for/each loop to read each line of
# the input file into a variable named 'theLine'
for line in f_cities:
    theLine = line

    # Increment the line count
    count += 1

    # Add the line number to the front of the line followed by a space
    theLine = f"{count} {theLine}"

    # print the line to the display
    print(theLine)

    # Write the new line to the output file
    f_cities_numbered.write(theLine)

# Close the input file
f_cities.close()

# Close the output file
f_cities_numbered.close()