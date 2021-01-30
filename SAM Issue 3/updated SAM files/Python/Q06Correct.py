#-------------------------------------------------------------------------------
# Name:        Artists
# Purpose:
#
# Author:      CSelby
#
# Created:     02/06/2016
# Copyright:   (c) CSelby 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

theArtists = [["Andy", "Warhol", 1928],
              ["Pablo", "Picasso", 1881],
              ["Salvador", "Dali", 1904],
              ["Lavinia", "Fontana", 1552],
              ["Jackson", "Pollock", 1912],
              ["Henri", "Matisse", 1869],
              ["Frida", "Kahlo", 1907],
              ["Georgia", "O'Keeffe", 1887],
              ["Kara", "Walker", 1969],
              ["Yayoi", "Kusama", 1929]
             ]

theLabels = []   # Put the new user labels into this structure

# Make the artist labels
for person in theArtists:
    newRecord = person[1][0] + person[0][0] + str(person[2])
    theLabels.append (newRecord)
print ("The new userIDs are: ", theLabels)

# Find and print the youngest person and their birthdate
maxDate = 0
for person in theArtists:
    if person[2] > maxDate:
        maxDate = person[2]
        maxPerson = person
print (maxPerson[0], maxPerson[1], "is youngest", str(maxPerson[2]))


