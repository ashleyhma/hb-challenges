def playlist(songs):
    count = 0 

    for idx1 in range(len(songs)):
        for idx2 in range(len(songs)):
            if idx2 > idx1:
                if (songs[idx2] + songs[idx1]) % 60 == 0:
                    count += 1 
    return count
                

