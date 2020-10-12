#!/usr/bin/env python3
#--------------------------------+
# Script Name   : max_of_three.py    
# Description   : Count max of three without using max()              
# Author        : Seth Acuesta   
# Date          : 10/12/2020
#--------------------------------+
import sys
inp = []

# Loop the 2nd args to last of the input (1st arg is the filename)
try:
    for args in sys.argv[1:]:
        inp.append(int(args))
except:
    inp = [5,10,15,-5]


def max_of_three(inp):

    m = 0
    for i in inp:
    
        if (i > m):
            m = i
    return m

if __name__ == '__main__':
    print(max_of_three(inp))
