# average of 365 temperatures held in an array of real numbers called temperature


temperature = [ ]
temperatureSum = 0

# 365 values
for i in range(0,73): temperature.append(i)
for i in range(0,73): temperature.append(i)
for i in range(0,73): temperature.append(i)
for i in range(0,73): temperature.append(i)
for i in range(0,73): temperature.append(i)

for n in temperature:
  temperatureSum = temperatureSum + n
  continue

print(temperatureSum / 365)
