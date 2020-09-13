#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the viralAdvertising function below.
def viralAdvertising(n):
    cumilativeLikes = 2
    likes = 2
    for i in range(1,n):
        likes = (3*likes)//2
        cumilativeLikes += likes
    return cumilativeLikes

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()