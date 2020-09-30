"""
Write a function called numbers in your testing_functions.py file. 
Use parameters to pass two numbers into the function. 
The function must then count from the first number to the second number. 
"""

def numbers(num1, num2):
  for i in range(num1, num2+1):
    print(i)
  if num1 > num2:
    count = num1
    while count >= num2:
      print(count)
      count = count - 1

numbers(2, 7)
print("________")
numbers(7, 2)