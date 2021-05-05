# -*- coding: utf-8 -*-
"""
Created on Sun May  2 15:26:04 2021

@author: Qilin Wang
"""

class Rectangle:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def calculate_perimeter(self):
        return 2 * (self.a + self.b)

class Square(Rectangle):
    def __init__(self,a):
        self.a = a
        self.b = a

if __name__ == '__main__':
    t1 = Rectangle(5,12)
    print(t1.calculate_perimeter())
    t2 = Square(12)
    print(t2.calculate_perimeter())