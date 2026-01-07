#!/bin/python3
# https://www.hackerrank.com/challenges/30-2d-arrays/problem?isFullScreen=true

import math
import os
import random
import re
import sys



if __name__ == '__main__':

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    
    
    suma = 0
    total = float("-inf")
    for i in range(4):
        
        for j in range(4):
            suma = (
                arr[i][j] + arr[i][j+1] + arr[i][j+2] + 
                arr[i+1][j+1] + 
                arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            )
            if suma >total:
                total = suma
                
    print(int(total))
            
