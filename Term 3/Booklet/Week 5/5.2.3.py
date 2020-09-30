name = 'max'
name_list = ['Anya', 'Max', 'Erik', 'William', 'David',
            'Shirley', 'Cheryl', 'Ben', 'Rosie', 'Henry', 'Georgina']
is_name = False

# sort list by alphabetical order
"""name_list.sort()
print(name_list)"""

# bubble sort
swapped = True
count = 0

while swapped == True:
  swapped = False
  for i in range(len(name_list)-1):
    if name_list[i] > name_list[i+1]:
      count += 1
      name_list[i], name_list[i+1] = name_list[i+1], name_list[i]
      swapped = True

print(name_list)
print(f"Count {count}")

print(f"\nSearching for: '{name}'\n")

# linear search
while is_name == False:
  for i in name_list:
    if name.lower() == i.lower():
      is_name = True
      print(is_name)
      print(i)
      break
    else:
      continue
  if is_name == False:
    print(is_name, '-', f"the name, '{name}', was not found")
    break
