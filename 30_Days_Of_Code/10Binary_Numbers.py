#!/bin/python3
#https://www.hackerrank.com/challenges/30-binary-numbers/problem?isFullScreen=true

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    aux = 0
    contador = 0
    while n >= 1: 
        bit = n%2
        if bit == 1:
            contador+=1
        if contador > aux:
                aux = contador
        if bit == 0:
                contador = 0
        n = n//2
        

    print(aux)
