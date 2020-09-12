# #!/bin/python3

# import math
# import os
# import random
# import re
# import sys

# #
# # Complete the 'climbingLeaderboard' function below.
# #
# # The function is expected to return an INTEGER_ARRAY.
# # The function accepts following parameters:
# #  1. INTEGER_ARRAY ranked
# #  2. INTEGER_ARRAY player
# #
# #TODO kacinci siradan itibaren bakmasi gerektigine bak ya da ters yonden baslat
# def findRank(ranked, score):
#     if score >= ranked[0]:
#         return 1
#     playerRank = 1
#     previousRank = ranked[0]
#     for rank in ranked:
#         if rank < previousRank and score < rank:
#             playerRank += 1
#             previousRank = rank
#         elif rank == previousRank and score < rank:
#             pass
#         else:
#             break
#     playerRank += 1
#     return playerRank

# def climbingLeaderboard(ranked, player):
#     # Write your code here
#     result = []

#     for score in player:
#         result.append(findRank(ranked, score))

#     return result

# if __name__ == '__main__':
    

#     result = climbingLeaderboard([100, 90, 90, 80, 75, 60], [50, 65, 77, 90, 102])
#     print(result)



#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#

def findRank(reducedRanked, score, previousRank):
    for i in range(previousRank - 1, len(reducedRanked)):
        if score >= reducedRanked[i]:
            return i + 1
    return len(reducedRanked) + 1
    

def climbingLeaderboard(ranked, player):
    # Write your code here
    result = []
    reducedRanked = [ranked[0]]
    previousRanked = ranked[0]
    for rank in ranked:
        if rank != previousRanked:
            previousRanked = rank
            reducedRanked.append(rank)
    rank = 1
    for i in range(len(player)-1, -1, -1):
        rank = findRank(reducedRanked, player[i], rank)
        result.insert(0, rank)

    return result

            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
