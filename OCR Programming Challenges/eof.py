with open("OCR Programming Challenges/file.txt", "r") as fp:
    text = fp.read()

for i in text:
    if i is None:
        print(i)