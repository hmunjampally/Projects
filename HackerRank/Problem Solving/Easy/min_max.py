#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    n = len(arr)
    sums = []
    new = sum(arr)
    for i in range(n):
        sums.append(new-arr[i])
    print(min(sums), max(sums))
    
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
