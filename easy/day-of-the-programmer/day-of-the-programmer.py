#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the dayOfProgrammer function below.
def dayOfProgrammer(year):
    d = 13
    if not (year % 4) and (year < 1918 or year % 100 or not (year % 400)):
        d -= 1
    if year == 1918:
        d = 26
    return str(d) + ".09." + str(year)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
