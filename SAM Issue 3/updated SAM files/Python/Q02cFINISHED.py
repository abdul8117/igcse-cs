myList = [(800, 23000), (1499, 10000), (1600, 47000), (200, 10000)]

for pair in myList:
    income = pair[1]
    attendance = pair[0]
    print ("Attendance: ", attendance, " income: ", income)

    if (attendance >= 1500) or (income >= 45000):
        print ("Sufficient profit made this week")
    elif (attendance >= 750) or (income >= 22500):
        print ("income in line with attendance this week")
    elif (attendance < 500):
        print ("Attendance is very low this week.  Contact the fan club.")
    else:
    	print("Possible accounting error")
