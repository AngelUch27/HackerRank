# https://www.hackerrank.com/challenges/30-sorting/problem?isFullScreen=true
#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))
    
    swaps =100
    total = 0
    # Write your code here
    while swaps > 0:
        swaps = 0
        for i in range(n-1):
            if a[i] > a[i+1]:
                aux = a[i]
                a[i] = a[i+1]
                a[i+1] = aux
                swaps +=1
        
        total +=swaps    
        
    print("Array is sorted in",total,"swaps.")
    print("First Element:",a[0])
    print("Last Element:",a[n-1])
