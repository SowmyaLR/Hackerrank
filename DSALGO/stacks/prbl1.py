#!/bin/python3
# https://www.hackerrank.com/challenges/balanced-brackets/problem
import math
import os
import random
import re
import sys

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isBalanced(s):
    # Write your code here
    if s == "":
        return "YES"
    if len(s)%2 == 1:
        return "NO"
    if s[0] == "}" or s[0] == ")" or s[0] == "]":
        return "NO"
    stk = []
    match = {
        ")": "(",
        "}": "{",
        "]": "["
    }
    for ch in s:
        if ch == "[" or ch == "{" or ch == "(":
            stk.append(ch)
        elif ch == "}" or ch == ")" or ch == "]":
            if len(stk) == 0:
                return "NO"
            if stk[len(stk)-1] != match[ch]:
                return "NO"
            stk.pop(len(stk)-1)
    if len(stk) != 0:
        return "NO"
    return "YES"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
