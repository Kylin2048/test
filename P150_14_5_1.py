# -*- coding: utf-8 -*-
"""
Created on Mon May  3 23:46:01 2021

@author: Qilin Wang
"""


class Square():
    square_list = []
    def __init__(self,a):
        self.a = a
        self.square_list.append(self)

s1 = Square(10)
s2 = Square(20)
s3 = Square(5)
for x in Square.square_list:
    print(x.a)