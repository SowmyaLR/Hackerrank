# https://www.hackerrank.com/challenges/truck-tour/problem

# !/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'truckTour' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY petrolpumps as parameter.
#

def truckTour(petrolpumps):
    # Write your code here
    tank = 0
    res = 0
    i = 0
    for pp in petrolpumps:
        tank += pp[0]
        if pp[1] <= tank:
            tank -= pp[1]
        else:
            tank = 0
            res = i + 1
        i = i + 1
    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    petrolpumps = []

    for _ in range(n):
        petrolpumps.append(list(map(int, input().rstrip().split())))

    result = truckTour(petrolpumps)

    fptr.write(str(result) + '\n')

    fptr.close()
