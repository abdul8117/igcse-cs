"""
print "Enter time in seconds for each pupil:"
SET pupil1Time TO INPUT("Time for pupil 1: ")
SET pupil2Time TO INPUT("Time for pupil 2: ")
SET pupil3Time TO INPUT("Time for pupil 3: ")

SET avg TO ( pupil1Time + pupil2Time + pupil3Time ) / 3
print "Average time:", avg
"""

from decimal import Decimal

print("Enter time in seconds for each pupil:")
pupil1Time = int(input("Pupil 1:"))
pupil2Time = int(input("Pupil 2:"))
pupil3Time = int(input("Pupil 3:"))

avg =  (pupil1Time + pupil2Time + pupil3Time) / 3
print("Average time:", round(avg, 2), "seconds")