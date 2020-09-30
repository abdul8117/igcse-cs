# # binary search
list = [837, 1529, 1683, 2245, 3901, 3921, 4524]
pupilNum = 1
found = False
first = 0
last = len(list)-1

while (first <= last and not found):
  middle = first + last // 2

  if list[middle] == pupilNum:
    found = True

  if pupilNum < list[middle]:
    last = middle - 1
  else:
    last = middle + 1

print(f"\n{found}")