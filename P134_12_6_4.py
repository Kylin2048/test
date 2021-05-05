# -*- coding: utf-8 -*-
"""
Created on Sun May  2 15:22:15 2021

@author: Qilin Wang
"""

class Hexagon:
    def __init__(self,r):
        self.rad = r
    def cacculate_perimeter(self):
        return self.rad * 6

t = Hexagon(10)
print(t.cacculate_perimeter())