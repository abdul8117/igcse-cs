# 1 = fToC    ,   2- cToF
conversion_choice = input("Do you want to convert from fahrenheit to celsius [1] or celsius to fahrenheit [2]?\n")
temp = int(input("Value: "))

def celsiusToFahrenheit(temperature_input):
  formula_cToF = (temperature_input * (9/5)) + 32
  result_cToF = formula_cToF
  print(round(result_cToF, 0), 'F')
  return temperature_input

def fahrenheitToCelsius(temperature_input):
  formula_fToC = (temperature_input - 32) * (5/9)
  result_fToC = formula_fToC 
  print(round(result_fToC, 0), 'C')
  return temperature_input

if conversion_choice == '1': fahrenheitToCelsius(temp)
else: celsiusToFahrenheit(temp)