# https://www.hackerrank.com/challenges/poisonous-plants/problem

# !/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'poisonousPlants' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY p as parameter.
#
def is_descending(arr):
    # print("arr", arr)
    for i in range(0, len(arr) - 1):
        if arr[i] < arr[i + 1]:
            # print("i", i)
            return False
    return True


def poisonousPlants(p):
    # Write your code here
    flag = 0
    cnt = 0
    while flag >= 0:
        for i in range(len(p) - 1, 0, -1):
            if p[i] > p[i - 1]:
                flag = 1
                p.pop(i)
        if flag == 1:
            cnt += 1
        else:
            break
        flag = 0
    return cnt


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = list(map(int, input().rstrip().split()))

    result = poisonousPlants(p)

    fptr.write(str(result) + '\n')

    fptr.close()
