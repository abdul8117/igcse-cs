lyrics = ["Sittin' in the mornin' sun",
          "I'll be sittin' when the evenin' comes",
          "Watchin' the ships roll in",
          "Then I watch 'em roll away again",
          "I'm sittin' on the dock of the bay"]


def writeToFile():
    myFile = open("newFile.txt", "w")
    for each in range(1, 8):
        record_0 = "This is record number {0} in the file - Abdul\n".format(each)
        print(record_0)
        myFile.write(record_0)
    myFile.close()

#main program
writeToFile()


def readFromFile():
    myFile = open("newFile.txt", "r")
    for each in range(1, 8):
        record_1 = myFile.readline()
        print(each, record_1)
    myFile.close()

def writeSongLyrics():
  myFile = open("newFile.txt", "a")
  for line in lyrics:
    record_lyrics = line + '\n'
    print(record_lyrics)
    myFile.write(record_lyrics)
  myFile.close

#main program
readFromFile()
writeSongLyrics()


def appendToFile():
  myFile = open("newFile.txt", "a")
  for each in range(1, 8):
    lineNum = each + 7
    record_2 = "This is record number {0} in the file \n".format(lineNum)
    myFile.write(record_2)
  myFile.close()

#main program
appendToFile()
