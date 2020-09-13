#!/bin/python3

import math
import os
import random
import re
import sys

def findReverse(n):
    stringN = str(n)
    reverseStringN = ""
    for i in range(len(stringN)-1, -1, -1):
        reverseStringN += stringN[i]
    return int(reverseStringN)



# Complete the beautifulDays function below.
def beautifulDays(i, j, k):
    result = 0
    for i in range(i, j+1):
        if abs(i - findReverse(i)) % k == 0:
            result += 1
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ijk = input().split()

    i = int(ijk[0])

    j = int(ijk[1])

    k = int(ijk[2])

    result = beautifulDays(i, j, k)

    fptr.write(str(result) + '\n')

    fptr.close()
