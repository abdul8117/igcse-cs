def option1():
    print("Option 1")

def option2():
    print("Option 2")

def option3():
    print("Option 3")

def get_input():
    user_input = input("Enter option: ")

    if user_input == "1":
        option1()
    elif user_input == "2":
        option2()
    elif user_input == "3":
        option3()
    else:
        get_input()


get_input()