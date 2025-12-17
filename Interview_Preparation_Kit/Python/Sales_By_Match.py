#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    # Write your code here
    ar.sort()
    aux = ar[0]
    contador = 0
    pares = 0
    for i in range(n):
        if ar[i] <= aux:
            contador +=1
        if ar[i] > aux:
            pares += contador//2
            contador = 1
            aux = ar[i]
            
    pares += contador//2
    return pares
            
        
        
            
            
    

        
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
