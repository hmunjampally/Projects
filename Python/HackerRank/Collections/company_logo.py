#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter, OrderedDict


if __name__ == '__main__':
    s = input()

    val = sorted(Counter(s).items(), key=lambda x: (-x[1], x[0]) )
    
    for i in val[:3]:
        print(i[0],i[1])
  
    