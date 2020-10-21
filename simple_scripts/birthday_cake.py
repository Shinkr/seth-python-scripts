#!/usr/bin/env python3
#--------------------------------+
# Script Name   : count_cake.py    
# Description   : count occurances of max value of cake   
# Author        : Seth Acuesta   
# Date          : 10/22/2020
# Source        : https://www.hackerrank.com/challenges/birthday-cake-candles/
#--------------------------------+
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    
    topval = max(candles)
    topcnt = 0

    for cc in candles:
        if (cc == topval):
            topcnt+= 1
    
    return topcnt


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()