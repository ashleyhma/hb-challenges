def hourglassSum(arr):
    """There are  hourglasses in , and an hourglass sum is the sum of an hourglass' values. Calculate the hourglass sum for every hourglass in , then print the maximum hourglass sum."""

    largest = -100

    
    for i in range(len(arr) - 2):
        for j in range(len(arr) - 2):
            row1 = arr[i][j] + arr[i][j+1] + arr[i][j+2]
            row2 = arr[i+1][j+1]
            row3 = arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            s = row1 + row2 + row3
            if s > largest:
                largest = s
             
    
    return largest
    