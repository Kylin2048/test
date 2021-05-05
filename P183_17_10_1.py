# -*- coding: utf-8 -*-
"""
Created on Wed May  5 15:39:14 2021

@author: Qilin Wang
"""

import re

with open('zen.txt','r') as f:
    st = f.read()
    
res = re.findall('Dutch',st,re.IGNORECASE)
print(res)