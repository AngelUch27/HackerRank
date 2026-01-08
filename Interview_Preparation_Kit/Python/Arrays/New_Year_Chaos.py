#!/bin/python3
# https://www.hackerrank.com/challenges/new-year-chaos/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

def minimumBribes(q):
    # Write your code here"
    maximo = 0

    for i in range(len(q)):
        start = max(0, q[i] - 2)
        diferencia = q[i]-(i+1)
        if diferencia>2:
            print("Too chaotic")
            return
        for j in range(start, i):
            if q[j] > q[i]:
                maximo += 1

    print(maximo)

            
        
        

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
