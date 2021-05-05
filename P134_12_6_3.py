# -*- coding: utf-8 -*-
"""
Created on Sun May  2 15:15:51 2021

@author: Qilin Wang
"""

class Triangle:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
    def area(self):
        import math
        return(math.sqrt((self.a+self.b+self.c)*
                         (self.a+self.b-self.c)*
                         (self.a-self.b+self.c)*
                         (-self.a+self.b+self.c))/4)
        
t = Triangle(5, 12, 13)
print(t.area())