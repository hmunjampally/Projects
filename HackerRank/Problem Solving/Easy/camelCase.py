#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'camelcase' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def camelcase(s):
    words = 1
    for i in s:
        if ord(i) >= 97 and ord(i) <= 122:
            words = words
        if ord(i) >= 65 and ord(i) <= 90:
            words += 1
            
    return words

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = camelcase(s)

    fptr.write(str(result) + '\n')

    fptr.close()
