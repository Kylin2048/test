# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 22:50:23 2021
4.12.5
@author: Qilin Wang
"""

def str2float (st):
    '''
    check whether str a string format float
    return float or invalid input
    
    '''
    try:
        x = float (st)
    except (ValueError):
        return "Invalid input"
    return x

print (str2float (input ("Type a decimal:")))