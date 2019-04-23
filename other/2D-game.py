
board = [
  [0,  0,  0, -1, -1],
  [0,  0, -1,  0,  0],
  [0, -1,  0, -1,  0],
  [0,  0, -1,  0,  0],
  [0,  0,  0,  0,  0],
  [0,  0,  0,  0,  0],
  [0,  0,  0,  0,  0],
]
start1 = [3, 1]
start2 = [5, 3]
start3 = [6, 0]
start4 = [6, 4]
start5 = [0, 0]
start6 = [2, 2]

def two_d(board, start):
    a = (start[0], start[1] - 1)
    b = (start[0], start[1] + 1)
    c = (start[0]+1, start[1])
    d = (start[0]-1, start[1])
    possible = [a, b, c, d]
    result = []

    for tup in possible:
        zero = tup[0]
        one = tup[1]
        if board[zero][one] != -1:
            result.append(tup)
    
    return result
    

