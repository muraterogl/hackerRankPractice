#!/bin/python3

import math
import os
import random
import re
import sys
magicSquares = [[[2, 7, 6], [9, 5, 1], [4, 3, 8]],
                [[2, 9, 4], [7, 5, 3], [6, 1, 8]],
                [[4, 3, 8], [9, 5, 1], [2, 7, 6]],
                [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
                [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
                [[6, 7, 2], [1, 5, 9], [8, 3, 4]],
                [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
                [[8, 3, 4], [1, 5, 9], [6, 7, 2]]]
# Complete the formingMagicSquare function below.
def formingMagicSquare(s):
    costs = []
    for magicSquare in magicSquares:
        cost = 0
        for i in range(len(s)):
            for j in range(len(s[0])):
                cost += abs(s[i][j] - magicSquare[i][j])
        costs.append(cost)
    return min(costs)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    fptr.write(str(result) + '\n')

    fptr.close()





# TO FIND ALL MAGIC SQUARES
# from itertools import permutations

# perm = permutations([1, 2, 3, 4, 5, 6, 7, 8, 9]) 

# for i in list(perm): 
#     if i[0] + i[1] + i[2] == 15 and i[3] + i[4] + i[5] == 15 and i[6] + i[7] + i[8] == 15 and i[0] + i[3] + i[6] == 15 and i[1] + i[4] + i[7] == 15 and i[2] + i[5] + i[8] == 15 and i[6] + i[4] + i[2] == 15 and i[0] + i[4] + i[8] == 15:
#         print(i)