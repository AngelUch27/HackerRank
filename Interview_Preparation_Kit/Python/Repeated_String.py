#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#
import math

def repeatedString(s, n):
    # Write your code here
    na = 0
    for i in range(len(s)):
        if s[i] == 'a':
            na += 1

    palabras = n // len(s)           
    first = palabras * na            

    rem = n % len(s)                 
    na2 = 0
    for i in range(rem):
        if s[i] == 'a':
            na2 += 1

    return first + na2

    
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
