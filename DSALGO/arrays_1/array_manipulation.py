#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'arrayManipulation' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#
def modify_array(a, b, k, arr, n):
    arr[a] += k
    if b + 1 <= n:
        arr[b + 1] -= k
    return arr


def arrayManipulation(n, queries):
    # Write your code here
    arr = []
    max_sum = 0
    cur_sum = 0
    for i in range(0, n + 1):
        arr.append(0)
    for q in queries:
        a = q[0]
        b = q[1]
        k = q[2]
        modify_array(a, b, k, arr, n)
    for i in range(1, n + 1):
        cur_sum += arr[i]
        if cur_sum > max_sum:
            max_sum = cur_sum
    return max_sum


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
