with open("OCR Programming Challenges/file.txt", "r") as fp:
    text = fp.read()

# print(text)

# number of charachters
print("Number of characters:", len(text))

# count the instances of 'the'
split = text.split()
count = 0

for word in split:
    if word == "the":
        count += 1

print("Instances of 'the':", count)

# count the instances of words starting with 'a'
split = text.split()
count = 0

for word in split:
    if word[0] == "a":
        count += 1

print("Instances of 'a':", count)


# question 4, 5 in read-2-files.py


# question 6
# read text, write it in another file but backwards
with open("OCR Programming Challenges/backwards.txt", "w") as fp:
    index = len(text) - 1
    backwards = ""

    while index >= 0:
        backwards += text[index]
        index -= 1
        
    fp.write(backwards)