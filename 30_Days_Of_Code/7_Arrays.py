#!/bin/python3
# https://www.hackerrank.com/challenges/30-arrays/problem?isFullScreen=true
import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    for i in range(n-1, -1,-1):
        print(arr[i],end=" ")
