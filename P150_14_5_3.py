# -*- coding: utf-8 -*-
"""
Created on Mon May  3 23:58:07 2021

@author: Qilin Wang
"""

def same(a,b):
    if a is b:
        return True
    else:
        return False

class Square():
    def __init__(self,a):
        self.a = a
        
a = Square(10)
b = a
c = Square(10)
print(same(a,b))
print(same(b,c))