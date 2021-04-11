text = "gayle is best than kohli how can you compare lion with rat"
output = ""
x = 0

for char in text:
    if x % 2 == 0:
        output += char.lower()
        x += 1
    else:
        output += char.upper()
        x += 1

    if char == " ":
        x -= 1


print(output)