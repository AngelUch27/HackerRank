#!/bin/python3
# https://www.hackerrank.com/challenges/30-recursion/problem?isFullScreen=true

import math
import os
import random
import re
import sys

#
# Complete the 'factorial' function below.
## The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def Factorial(n):
    # Write your code here
    if n<=1:
        return 1
    return n * Factorial(n-1)
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = Factorial(n)

    fptr.write(str(result) + '\n')

    fptr.close()
