import time

theDate = ""

def toCelsius (inTemp):
    celsius = 0
    celsius = (5.0 / 9.0) * (inTemp - 32.0)
    return (celsius)

def toFahrenheit (inTemp):
    fahrenheit = ((9.0 / 5.0) * inTemp) + 32.0
    return (fahrenheit)

def waitTenSeconds ():
    time.sleep (10)

def waitTime (inSeconds):
    time.sleep (inSeconds)

print (toFahrenheit (0))
print (toCelsius (212.0))   # This line does not work properly
print ("Sleeping for 10")
waitTenSeconds()
print (toCelsius (32.0))
print ("Sleeping for 5")
waitTime (5)
print (toFahrenheit (100.0))

