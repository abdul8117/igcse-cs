theArtists = [
                ["Andy", "Warhol", 1928],
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

# Add your code here
def generate_label(fName, lName, dateOfBirth):
   label = lName[0] + fName[0] + str(dateOfBirth)
   
   return label

def find_youngest_artist(artists):
   largest = 0
   smallest = 0

   for i in artists:
      if i[2] > largest:
         largest = i[2]


   for i in theArtists:
      if i[2] < largest:
         smallest = i[2]

   return smallest


def main():
   for artist in theArtists:
      first_name = artist[0]
      last_name = artist[1]
      date_of_birth = artist[2]

      theLabels.append(generate_label(first_name, last_name, date_of_birth))
   
   for i in theLabels:
      print(i)
   
   print(find_youngest_artist(theArtists))

main()