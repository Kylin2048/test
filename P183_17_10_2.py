# -*- coding: utf-8 -*-
"""
Created on Wed May  5 15:44:15 2021

@author: Qilin Wang
"""

import re

st = 'Arizona 479,501,870.Carlifornia 209,213,650.'

res = re.findall('\d',st)

print(res)