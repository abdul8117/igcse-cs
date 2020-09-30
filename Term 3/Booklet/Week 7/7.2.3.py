import csv

with open('c:/Users/user/OneDrive - GEMS EDUCATION/IGCSE/Y10/Computer Science/Term 3/Booklet/Week 7/scores.csv', newline='') as csvfile:
  reader = csv.reader(csvfile)
  for row in reader:
    print(row)