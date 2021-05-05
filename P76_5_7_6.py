# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 22:18:00 2021
set
@author: Qilin Wang
"""

a = range(2,10)
b = [2 ** x for x in a if x%2]
print(b)

c = [2 ** x for x in range(2,10)]
print(c)

sb = set(b)
sc = set(c)

print(sb)
print(sc)
print(sc-sb)