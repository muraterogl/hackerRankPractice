#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the acmTeam function below.
def acmTeam(topic):
    maxTopic = 0
    maxTopicCount = 0
    for i in range(len(topic)):
        for j in range(i+1, len(topic)):
            currentTopicCombination = bin(int(topic[i],2) | int(topic[j],2))[2:]
            currentMaxTopic = currentTopicCombination.count('1')
            if maxTopic < currentMaxTopic:
                maxTopic = currentMaxTopic
                maxTopicCount = 1
            elif maxTopic == currentMaxTopic:
                maxTopicCount += 1
    return (maxTopic,maxTopicCount)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
