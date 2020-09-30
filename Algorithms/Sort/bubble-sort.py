a = [2, 8, 5, 3, 9, 4, 1]
print(f"\n{a}\n\nv\n")
#a = ['Anya', 'Max', 'Erik', 'William', 'David', 'Shirley', 'Cheryl', 'Ben', 'Rosie', 'Henry', 'Georgina']
swapped = True

while swapped == True:
  swapped = False
  for i in range(len(a)-1):
    if a[i] > a[i+1]:
      a[i], a[i+1] = a[i+1], a[i]
      swapped = True

print(a)
