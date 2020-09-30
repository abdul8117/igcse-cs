age = 1
total = 0
count = 0
average = 0

while age > 0:
    age = int(input("Enter your age: "))
    total += age
    count += 1
count -= 1
average = total / count
print(average)
