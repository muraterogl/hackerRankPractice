#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    highestScore = scores[0]
    lowestScore = scores[0]
    highestCount = 0
    lowestCount = 0
    for score in scores:
        if score > highestScore:
            highestScore = score
            highestCount += 1
        elif score < lowestScore:
            lowestScore = score
            lowestCount += 1
    return [highestCount, lowestCount]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
