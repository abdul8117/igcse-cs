# loop through each character = i
# check every follwoing character until it != i
#  

string = "AAABBBBBCCC"
count = 0
index = 0
j = string[0]

for letter in string:
  letter = j
  while j == letter:
    if string[index+1] == letter:
      count += 1
      print(f"count {count}") 