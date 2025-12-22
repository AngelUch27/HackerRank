#!/bin/python3
#https://www.hackerrank.com/challenges/30-conditional-statements/problem?isFullScreen=true

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input().strip())
    if (N%2==0 and N >=2 and N <=5) or (N%2==0 and N>20):
        print('Not Weird')
    else:
        print('Weird')
    
        
