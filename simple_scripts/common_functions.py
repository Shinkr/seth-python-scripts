#!/usr/bin/env python3
#--------------------------------+
# Script Name   : get_input    
# Description   : Common functions   
# Author        : Seth Acuesta   
# Date          : 10/13/2020
#--------------------------------+
import sys

# Description : Get Input function / module so i don't have to put it on the code every time.
def get_input():
    
    inp = []
    
    try:
        for args in sys.argv[1:]:
            inp.append(int(args))
        return inp
    except:
        return [5, 10, 15, -5]
