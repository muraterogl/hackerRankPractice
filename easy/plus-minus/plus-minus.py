#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    pc = 0
    nc = 0
    zc = 0
    for num in arr:
        if num > 0:
            pc += 1
        elif num == 0:
            zc += 1
        else:
            nc += 1
    print('%.6f'%(pc/len(arr)))
    print('%.6f'%(nc/len(arr)))
    print('%.6f'%(zc/len(arr)))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
