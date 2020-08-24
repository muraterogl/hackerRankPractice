#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the queensAttack function below.
def queensAttack(n, k, r_q, c_q, obstacles):
    uNu = n - r_q
    ulNu = min(n - r_q, c_q - 1)
    lNu = c_q - 1
    ldNu = min(c_q - 1, r_q - 1)
    dNu = r_q - 1
    drNu = min(r_q - 1, n - c_q)
    rNu = n - c_q
    ruNu = min(n - c_q, n - r_q)
    for obstacle in obstacles:
        if obstacle[0] > r_q:
            if obstacle[1] > c_q:
                #potentialy, obstacle is on ru
                if (obstacle[0]- r_q) / (obstacle[1] - c_q) == 1:
                    if ruNu > obstacle[0]- r_q - 1:
                        ruNu = obstacle[0]- r_q - 1
            elif obstacle[1] < c_q:
                #potentialy, obstacle is on ul
                if (obstacle[0]- r_q) / (c_q - obstacle[1]) == 1:
                    if ulNu > obstacle[0]- r_q - 1:
                        ulNu = obstacle[0]- r_q - 1
            else:
                #obstacle is on u
                if uNu > obstacle[0] - r_q - 1:
                    uNu = obstacle[0] - r_q - 1
        elif obstacle[0] < r_q:
            if obstacle[1] > c_q:
                #potentialy, obstacle is on dr
                if (r_q - obstacle[0]) / (obstacle[1] - c_q) == 1:
                    if drNu > r_q - obstacle[0] - 1:
                        drNu = r_q - obstacle[0] -1
            elif obstacle[1] < c_q:
                #potentialy, obstacle is on ld
                if (r_q - obstacle[0]) / (c_q - obstacle[1]) == 1:
                    if ldNu > r_q - obstacle[0] - 1:
                        ldNu = r_q - obstacle[0] -1
            else:
                #obstacle is on d
                if dNu > r_q - obstacle[0] - 1:
                    dNu = r_q - obstacle[0] - 1
        else:
            if obstacle[1] > c_q:
                #obstacle is on r
                if rNu > obstacle[1] - c_q - 1:
                    rNu = obstacle[1] - c_q - 1
            elif obstacle[1] < c_q:
                #obstacle is on l
                if lNu > c_q - obstacle[1] - 1:
                    lNu = c_q - obstacle[1] - 1
            else:
                #we dont expect it here :)
                pass
    return uNu + ulNu + lNu + ldNu + dNu + drNu + rNu + ruNu


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    r_qC_q = input().split()

    r_q = int(r_qC_q[0])

    c_q = int(r_qC_q[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    fptr.write(str(result) + '\n')

    fptr.close()
