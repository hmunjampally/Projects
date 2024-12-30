#!/bin/python3

import math
import os
import random
import re
import sys

def plusMinus(arr):
    n = len(arr)
    pos = 0
    neg = 0
    zeros = 0
    for i in range(n):
        if arr[i]>0:
            pos += 1
        if arr[i]<0:
            neg += 1
        if arr[i] == 0:
            zeros += 1
    print(f"{pos/n:.6f}")
    print(f"{neg/n:.6f}")
    print(f"{zeros/n:.6f}")
    
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
