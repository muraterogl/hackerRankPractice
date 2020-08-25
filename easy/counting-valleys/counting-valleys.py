#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    currentLevel = 0
    valleyCount = 0
    mountainCount = 0
    for i in range(n):
        if s[i] == 'D':
            currentLevel -= 1
            if currentLevel == 0:
                mountainCount += 1
        else:
            currentLevel += 1
            if currentLevel == 0:
                valleyCount += 1
    return valleyCount

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
