#https://www.hackerrank.com/challenges/s10-standard-deviation/problem?isFullScreen=true
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'stdDev' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def stdDev(arr):
    # Print your answers to 1 decimal place within this function
    media = sum(arr)/len(arr)
    res = 0
    for elemento in arr:
        res+=(elemento-media)**2
    res=(res/len(arr)) ** .5
    
    print(f"{res:.1f}")   
    
    
        

if __name__ == '__main__':
    n = int(input().strip())

    vals = list(map(int, input().rstrip().split()))

    stdDev(vals)
