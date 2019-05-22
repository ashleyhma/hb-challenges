def rotate(self, matrix):
    """
    Given input matrix = 
    [
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ],

    rotate the input matrix in-place such that it becomes:
    [
    [7,4,1],
    [8,5,2],
    [9,6,3]
    ]
    """
    
    matrix.reverse()
    
    for i in range(len(matrix)):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    return matrix