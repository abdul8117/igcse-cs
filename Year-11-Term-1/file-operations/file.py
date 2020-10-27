f = open(r"Year-11-Term-1\file-operations\file.txt", "r")
file_content = f.read()

for i in file_content:
  if i.isnumeric():
    print("The file has numbers.")
    break

f.close()