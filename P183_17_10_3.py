# -*- coding: utf-8 -*-
"""
Created on Wed May  5 15:46:20 2021

@author: Qilin Wang
"""

import re

st = 'The ghost that says boo huants the loo.'

res = re.findall('.oo',st,re.IGNORECASE)

print(res)