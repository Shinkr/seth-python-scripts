#!/usr/bin/env python3
#--------------------------------+
# Script Name   : getsumarray    
# Description   : Gets sum of Array Input               
# Author        : Seth Acuesta   
# Date          : 10/10/2020
#--------------------------------+

import os
import sys

def simpleArraySum(ar):
    ctr = 0
    for a in ar:
        ctr += a
    return ctr

if __name__ == '__main__':
    print(simpleArraySum([5, 10, 15, 20]))