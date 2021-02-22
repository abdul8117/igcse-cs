mark1 = int(input("Mark 1: "))
mark2 = int(input("Mark 2: "))
mark3 = int(input("Mark 3: "))

if mark1 > mark2:
    if mark1 > mark3:
        print(mark1)
    else:
        print(mark3)
else:
    if mark2 > mark3:
        print(mark2)
    else:
        print(mark3)

    
