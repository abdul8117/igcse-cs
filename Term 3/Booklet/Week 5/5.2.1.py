# sum and mean from a list
"""
SET numbers TO [list of numbers]
SET sum TO 0
SET mean TO 0
SET count TO 0

for each num in numbers
  sum = sum + num
  increment count

mean = sum / count
"""

numbers = [12, 19, 3, 22, 15, 9, 32, 50, 1, 41, 11, 8, 4, 91, 5]
sumOfNumbers = 0
mean = 0
count = 0

for number in numbers:
  sumOfNumbers += number
  count += 1

mean = sumOfNumbers / count

print("List:", numbers)
print("Sum:", sumOfNumbers)
print("Mean:", round(mean, 2))