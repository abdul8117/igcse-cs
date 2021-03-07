import random, time

a = random.sample(range(10000), 10000)
#a = ['Anya', 'Max', 'Erik', 'William', 'David', 'Shirley', 'Cheryl', 'Ben', 'Rosie', 'Henry', 'Georgina']

swapped = True

while swapped == True:
  swapped = False
  for i in range(len(a)-1):
    if a[i] > a[i+1]:
      a[i], a[i+1] = a[i+1], a[i]
      swapped = True

# print(a)
print(time.perf_counter())

# 10,000 numbers, 61.80s