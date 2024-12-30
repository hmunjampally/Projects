import math
import os
import random
import re
import sys


def timeConversion(s):
    x = s.split(":")[0]
    y = s.split(":")[-1]
    
    if "PM" in y and int(x)<12:
        new = 12 + int(x)
    if "AM" in y and int(x)==12:
        new = "00"
    if "PM" in y and int(x)==12:
        new = "12"
    if "AM" in y and int(x)<12:
        new=x
        
    return str(new)+":"+s.split(":")[1]+":"+y[0:2]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()
    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
