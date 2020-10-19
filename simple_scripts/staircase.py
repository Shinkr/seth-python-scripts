#!/usr/bin/env python3
#--------------------------------+
# Script Name   : staircase.py    
# Description   : make staircase based on input number 
# Author        : Seth Acuesta   
# Date          : 10/19/2020
#--------------------------------+
import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    ctr = 1
    
    
    # First loop
    while (ctr <= n):
        
        out = ""
        placeholder = []

        # FILLS THE PLACEHOLDER LIST WITH X
        while (len(placeholder) != (n - ctr)):
            placeholder.append(" ")

        while (len(placeholder) != n):
            placeholder.append("#")

        for p in placeholder:
            out += p

        print (out)
        ctr+= 1

if __name__ == '__main__':
    n = int(input())

    staircase(n)
