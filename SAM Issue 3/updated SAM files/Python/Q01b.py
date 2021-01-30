x = 44
t = 0

for i in range(0, 60):
    t = t + i - x + 12
    if(i >= 10):
        print(i * 10 / 14)
    else:
        print(i)
        
print(t)
