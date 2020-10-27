# marks = ['Amy', 'Jones', 'English', 67, 'Maths', 76, 'Computer Science', 96]
marks = {
  "name": 'Amy Jones',
  "english": 67,
  "maths": 76,
  "computer science": 96
}

index = 0
for i, j in marks:
  if i == "english":
    j = 76

marks.pop("maths")

# calculate avg
sum_ = 0
count = 0

for i, j in marks:
  if isinstance(j, int):
    sum_ += i
    count += 1

print(f"{sum_/count}")



print(marks)