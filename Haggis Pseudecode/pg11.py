totalRunningTime = 0

numberOfTracks = 0


while numberOfTracks < 1 or numberOfTracks > 20:
  try:
    print("You can only burn between 1 and 20 tracks.")
  except:
    print("Invalid input.")
    continue
