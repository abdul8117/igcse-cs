# Read file
# Split newlines

f = open("AQA-2021/Airports.txt", "r")
airports = f.read().split("\n")
print(airports)