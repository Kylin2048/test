# -*- coding: utf-8 -*-
"""
Created on Mon May  3 23:51:52 2021

@author: Qilin Wang
"""

class Square():
    square_list = []
    def __init__(self,a):
        self.a = a
        self.square_list.append(self)
    def __repr__(self):
        return ' by '.join([str(self.a) for x in range(4)])

s1 = Square(10)
s2 = Square(20)
s3 = Square(5)
print(Square.square_list)