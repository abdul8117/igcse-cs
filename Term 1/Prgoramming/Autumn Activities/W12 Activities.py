marks = ['Amy', 'Jones', 'English', 67, 'Maths', 76, 'Computer Science', 96]

for i, j in enumerate(marks):
  # i: index
  # j: item
  
  # update english mark
  if isinstance(j, str):
    if j.lower() == 'english':
      marks[i+1] = 72

  # remove maths
  if isinstance(j, str):
    if j.lower() == 'maths':
      del marks[i]
      del marks[i]

# add physics
marks.append("Physics")
marks.append(65)

# average mark
sum_ = 0
count = 0

for i in marks:
  if isinstance(i, int):
    sum_ += i
    count += 1

print(f"Average: {sum_ / count}")
print(marks)