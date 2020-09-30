print("Hello, this is the wage calculator.\n")

def get_credentials():

    global ni_number
    global emp_status
    global hours_worked
    global pay_rate

    ni_number = input("National Insurance number: ")
    emp_status = input("Employment status (f/p): ")
    hours_worked = float(input("Hours worked: "))
    pay_rate = float(input("Rate of pay: "))
    print("\n")

    # function for validation
    validate_credentials(ni_number, emp_status, hours_worked, pay_rate)

def validate_credentials(niNum, empStatus, hours, pay):

    if len(niNum) != 9:
        print("National Insurance number is invalid. Re-enter credentials.\n")
        get_credentials()
    elif hours < 0 or hours_worked > 50:
        print("Work hours entered in invalid. Re-enter credentials.\n")
        get_credentials()
    elif (empStatus == "p" and hours > 20) or (empStatus == "f" and hours > 50):
        print("Employment status does not match work hours. Re-enter credentials.\n")
        get_credentials()
    else:
        main(ni_number, emp_status, hours_worked, pay_rate)

def print_wage(hours, pay):
    print(f"Your salary for the week is: {hours * pay} QAR\n")

def main(niNum, empStatus, hours, pay):

    if empStatus == "p":
        empStatus = "Part-time"
    else: 
        empStatus = "Full-time"

    print(
        f"National Insurance Number: {niNum}\n" +
        f"Employment Status: {empStatus}\n" +
        f"Hours worked: {hours}\n" +
        f"Pay rate (hourly): {pay}\n"
    )

    valid = input(f"\nConfirm that these credentials are correct (y/n): ")
    print("\n")

    if valid == "n":
        get_credentials()

    print_wage(hours, pay)

# program runs through this one function 
get_credentials()