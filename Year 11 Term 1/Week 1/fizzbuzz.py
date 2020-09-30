# import time

# list = []
# num = 1

# while True:
#     list.append(num)

#     if list[-1] % 3 == 0 and list[-1] % 5 == 0: list[-1] = 'FizzBuzz'
#     elif list[-1] % 3 == 0 and not list[-1] % 5 == 0: list[-1] = 'Fizz'
#     elif list[-1] % 5 == 0 and not list[-1] % 3 == 0: list[-1] = 'Buzz'
    
#     print(list[-1])
#     num += 1
#     time.sleep(1)


"""
PSEUDOCODE

SET numbers = <list of numbers 1 to 100 inclusive>

FOR EACH in numbers
    SET output to ""

    if i mod 3 == 0
        <add "Fizz" to output>
    if i mod 5 == 0
        <add "Buzz" to output>

"""


numbers = [i for i in range(100+1)]

for i in numbers:
    output = ''
    
    if i % 3 == 0: output += 'Fizz'
    if i % 5 == 0: output += 'Buzz'

    if output == '': output = i

    print(output)