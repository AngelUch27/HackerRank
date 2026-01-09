#!/bin/python3
# https://www.hackerrank.com/challenges/30-exceptions-string-to-integer/problem
import math
import os
import random
import re
import sys


S = input().strip()
try:
    S=int(S)
    print(S)
except ValueError:
    print("Bad String")

