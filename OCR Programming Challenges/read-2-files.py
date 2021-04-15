with open("OCR Programming Challenges/file.txt", "r") as fp1, open("OCR Programming Challenges/file2.txt", "r") as fp2:
    text = fp1.read() + "\n" + fp2.read()

with open("OCR Programming Challenges/output-q4.txt", "w") as fp3:
    fp.writelines(text)


# q5
with open("OCR Programming Challenges/file3.txt") as fp4, open("OCR Programming Challenges/output-q4.txt") as fp5:
    fp5.writelines(fp4.read())


