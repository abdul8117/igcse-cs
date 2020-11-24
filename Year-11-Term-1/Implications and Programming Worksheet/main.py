# ask name
name = input("Name: ")

# ask times for each run
i = 0
times = []

while i < 7:
    time = int(input(f"Time {i+1}: "))
    times.append(time)
    i += 1

# print avg
print(f"Hello John, your average time is {round(sum(times) / 7, 0)}")

# print fastest and slowest times
print(f"Fastest time is {max(times)} and slowest time is {min(times)}")