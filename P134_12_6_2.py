# -*- coding: utf-8 -*-
"""
Created on Sun May  2 15:11:02 2021

@author: Qilin Wang
"""

class Circle:
    def __init__(self,r):
        self.rad = r
    def area(self):
        import math
        return self.rad ** 2 * math.pi

t = Circle(10)
print(t.area())
    