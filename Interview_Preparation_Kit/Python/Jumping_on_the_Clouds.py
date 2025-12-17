#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#

def jumpingOnClouds(c):
    # Write your code here\
    pos = 0
    jumps = 0
    while pos < len(c)-3:
        """if c[len(c)-1] == 0 and uno is False:
            uno = True
            jumps +=1"""
        if c[pos+2] != 1:
            pos+=2
            
        else:
            pos+=1
        
        jumps +=1
    if c[pos] == 0:
        jumps+=1
    return jumps
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
