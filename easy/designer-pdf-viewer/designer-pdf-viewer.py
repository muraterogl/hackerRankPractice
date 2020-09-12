#!/bin/python3

import math
import os
import random
import re
import sys

def char_position(letter):
    return ord(letter) - 97
# Complete the designerPdfViewer function below.
def designerPdfViewer(h, word):
    heights = []
    for letter in word:
        heights.append(h[char_position(letter)])
    return max(heights)*len(word)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()
