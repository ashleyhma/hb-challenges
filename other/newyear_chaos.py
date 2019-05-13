def minimumBribes(q):
    """Complete the function minimumBribes in the editor below. It must print an integer representing the minimum number of bribes necessary, or Too chaotic if the line configuration is not possible.

    minimumBribes has the following parameter(s):

    q: an array of integers"""
    
    c = False
    for i, v in enumerate(q):
        if v - i - 1 > 2:
            c = True

    count = 0
    swap = False
    for i in range(len(q)-1):
        for j in range(len(q)-1):
            if q[j] > q[j+1]:
                q[j], q[j+1] = q[j+1], q[j]
                count += 1 
                swap = True
        
        if swap:
            swap = False
        else:
            break

    if c == True:
        print("Too chaotic")
    else:         
        print(count)