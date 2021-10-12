# https://www.hackerrank.com/challenges/game-of-two-stacks/problem

# !/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'twoStacks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER maxSum
#  2. INTEGER_ARRAY a
#  3. INTEGER_ARRAY b
#

def twoStacks(maxSum, a, b):
    # Write your code here
    run_sum = 0
    cnt = 0
    n = len(a)
    m = len(b)
    i = 0
    j = 0
    while i < n and j < m:
        if a[i] <= b[j]:
            # print("if a", a[i], "b", b[j])
            rem = a[i]
            i += 1
        else:
            # print("else a", a[i], "b", b[j])
            rem = b[j]
            j += 1
        if rem + run_sum > maxSum:
            return cnt
        else:
            cnt += 1
            run_sum += rem
            # print("top ", rem, "run", run_sum)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input().strip())

    for g_itr in range(g):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        maxSum = int(first_multiple_input[2])

        a = list(map(int, input().rstrip().split()))

        b = list(map(int, input().rstrip().split()))

        result = twoStacks(maxSum, a, b)

        fptr.write(str(result) + '\n')

    fptr.close()
