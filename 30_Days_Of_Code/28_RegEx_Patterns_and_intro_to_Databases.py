# https://www.hackerrank.com/challenges/30-regex-patterns/problem?isFullScreen=true
#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input().strip())
    order_list = []
    for N_itr in range(N):
        first_multiple_input = input().rstrip().split()

        firstName = first_multiple_input[0]

        emailID = first_multiple_input[1]
        
        if re.search(r"@gmail\.com$", emailID):
            order_list.append(firstName)
            
    order_list.sort()
    for element in order_list:
        print(element)
        
        

        
