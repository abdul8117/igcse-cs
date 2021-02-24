total_running_time = 0


def get_title_and_lengths(numOfTracks):
    for i in range(numOfTracks):
        track_titles[i-1] = input("Track title: ")
        track_lengths[i-1] = int(input("Track length in seconds: "))



while True:
    numberOfTracks = int(input("Number of tracks: "))

    if numberOfTracks < 1 or numberOfTracks > 20:
        print("Please enter number of tracks between 1 and 20: ")
        continue
    else:
        break
    


track_titles = [0 for i in range(numberOfTracks - 1)]
track_lengths = [0 for i in range(numberOfTracks - 1)]
get_title_and_lengths(numberOfTracks)


for i in range(numberOfTracks-1):
    print(f"{track_titles[i]} and {track_lengths[i]} seconds")


print(f"{sum(track_lengths)}")


