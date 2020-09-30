week = ['Y', 'N', 'Y', 'Y', 'N', 'Y', 'N']
arrLength = len(week)
days = 0
index = 0

while True:
    if week[index] == 'Y':
        days += 1
    index += 1
    if index == arrLength:
        break

print(f"Extra staff were needed on {days} days")