#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    start = 1
    while start<=n:
        x = (n-start)*' '+ start*'#'
        print(x)
        start += 1

if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
