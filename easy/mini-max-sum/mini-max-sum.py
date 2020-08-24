#!/bin/python3

import math
import os
import random
import re
import sys
import functools

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    maxOfArray = max(arr)
    minOfArray = min(arr)
    sumTotal = sum(arr)
    print(str(sumTotal - maxOfArray) + " " + str(sumTotal - minOfArray))

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
