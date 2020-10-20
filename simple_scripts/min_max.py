#!/usr/bin/env python3
#--------------------------------+
# Script Name   : min_max.py    
# Description   : fetch list, find min max by adding values -1     
# Author        : Seth Acuesta   
# Date          : 10/20/2020
#--------------------------------+
import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):

    counter = 0
    ll = []

    while (counter != len(arr)):
        summ = 0
        for a in arr:
            summ += a
        val = summ - arr[counter]
        ll.append(val)
        counter+= 1

    maxx = max(ll)
    minn = min(ll)

    print (str(minn) + " " + str(maxx))
if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
