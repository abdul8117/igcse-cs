def functionOne():
  global answer
  number1 = 90 # local
  number2 = 78 # local
  answer = number1 * number2 # global

def functionTwo():
  global answer
  number1 = 65 # local
  number2 = 3 # local
  answer = number1 / number2 # global
