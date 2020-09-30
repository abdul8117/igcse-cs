visitors = [122, 51, 147, 91, 73, 124, 61]
index = 0
maximum = 0

while index < len(visitors):
  if visitors[index] > maximum:
    maximum = visitors[index]
  index += 1

print(f'The maximum number of visitors on any one day was {maximum}')

# for i in visitors:
#   if i > maximum:
#     maximum = i
# print(f'The maximum number of visitors on any one day was {maximum}')