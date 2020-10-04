"""
This algorithm implements the RLE compression method to a string.

Loop through each character starting with the first. 
Count the occurences of this letter following it until a different character is found.
Append the count and the letter to a separate string. 


AAABBBBBBBCCC
becomes 3A7B3C
"""

def rle_encode(string):

  # i is the index of the letter being checked for 
  # j is/are the following chars

  encoded = ""
  i = 0

  while i < len(string):
    curr_char = string[i]
    count = 1
    j = i

    while j < len(string)-1:
      if (string[j] == string[j+1]):
        count += 1
        j += 1
      else: 
        break
    
    encoded += str(count) + curr_char
    i = j + 1

  return encoded

usr_input = input("String: ")
encoded_string = rle_encode(usr_input)

print(encoded_string.replace("1", ""))