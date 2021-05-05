# -*- coding: utf-8 -*-
"""
Created on Sun May  2 13:54:35 2021

@author: Qilin Wang
"""

l1 = [8,19,148,4]
l2 = [9,1,33,83]
l3 = []
for i in l1:
    for j in l2:
        l3.append(i*j)
print(l3)