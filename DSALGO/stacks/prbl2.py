# https://www.hackerrank.com/challenges/equal-stacks/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'equalStacks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY h1
#  2. INTEGER_ARRAY h2
#  3. INTEGER_ARRAY h3
#
def add_reverse(arr):
    siz = len(arr)
    res = [arr[siz-1]]
    # print(res)
    j = 0
    for i in range(siz-2, -1, -1):
        # print(res[i])
        res.append(arr[i]+res[j])
        j += 1
    return res

def find_stack_size(a1, a2, a3):
    for i in a1:
        if i in a2 and i in a3:
            return i
    return 0

def equalStacks(h1, h2, h3):
    # Write your code here
    r1 = add_reverse(h1)
    r2 = add_reverse(h2)
    r3 = add_reverse(h3)
    sorted(r1, reverse=True)
    sorted(r2, reverse=True)
    sorted(r3, reverse=True)
    if (len(r1) <= len(r2)) and (len(r1) <= len(r3)):
        return find_stack_size(r1, r2, r3)
    elif (len(r2) <= len(r1)) and (len(r2) <= len(r3)):
        return find_stack_size(r2, r1, r3)
    else:
        return find_stack_size(r3, r2, r1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n1 = int(first_multiple_input[0])

    n2 = int(first_multiple_input[1])

    n3 = int(first_multiple_input[2])

    h1 = list(map(int, input().rstrip().split()))

    h2 = list(map(int, input().rstrip().split()))

    h3 = list(map(int, input().rstrip().split()))

    result = equalStacks(h1, h2, h3)

    fptr.write(str(result) + '\n')

    fptr.close()
