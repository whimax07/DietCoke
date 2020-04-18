import numpy as np
import time
import sys


def main():
    n = 15
    Square = [i + 1 for i in range(n) ]
    Square = np.array(Square, dtype='int8', ndmin=2)
    square = np.zeros([n-1, n], dtype='int8')
    Square = np.concatenate((Square, square), axis=0)
    #print(Square)
    Solver(Square, n)


def isValid(Square, x, y, z):
    for i in range(x):
        if Square[i][y] == z:
            return False
    for j in range(y):
        if Square[x][j] == z:
            return False
    return True


def Solver(Square, n):
    global tiker
    for j in range(n):
        for i in range(1, n):
            if Square[i][j] == 0:
                for z in range(1, n+1):
                    if isValid(Square, i, j, z):
                        Square[i][j] = z
                        tiker += 1
                        print(tiker)
                        Solver(Square, n)
                        Square[i][j] = 0
                return 

    print(np.matrix(Square)) 
    sys.exit()           
                

tiker = 0
main()

s11 = 4152
s12 = 9478
s13 = 55157
s14 = 1518744
s15 = 18763548
s15sq = \
    [[ 1,  2,  3, 4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15], \
    [ 2,  1,  4,  3,  6,  5,  8,  9,  7, 11, 10, 13, 12, 15, 14], \
    [ 3,  4,  1,  2,  7,  8,  5, 10, 11,  6,  9, 14, 15, 12, 13], \
    [ 4,  3,  2,  1,  8,  7,  6, 11, 10,  9,  5, 15, 14, 13, 12], \
    [ 5,  6,  7,  8,  1,  2,  3, 12, 13, 14, 15,  4,  9, 10, 11], \
    [ 6,  5,  8,  7,  2,  1,  4, 13, 12, 15, 14,  9,  3, 11, 10], \
    [ 7,  8,  5,  6,  3,  4,  1, 14, 15, 12, 13, 10, 11,  2,  9], \
    [ 8,  7,  6,  5,  4,  3,  2, 15, 14, 13, 12, 11, 10,  9,  1], \
    [ 9, 10, 11, 12, 13, 14, 15,  1,  2,  3,  4,  5,  6,  7,  8], \
    [10,  9, 12, 13, 11, 15, 14,  2,  1,  4,  3,  6,  5,  8,  7], \
    [11, 12,  9, 14, 15, 10, 13,  3,  4,  1,  2,  7,  8,  5,  6], \
    [12, 11, 10, 15, 14, 13,  9,  4,  3,  2,  1,  8,  7,  6,  5], \
    [13, 14, 15,  9, 10, 11, 12,  5,  6,  7,  8,  1,  2,  3,  4], \
    [14, 15, 13, 10,  9, 12, 11,  6,  5,  8,  7,  2,  1,  4,  3], \
    [15, 13, 14, 11, 12,  9, 10,  7,  8,  5,  6,  3,  4,  1,  2]]