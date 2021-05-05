# -*- coding: utf-8 -*-
"""
Created on Sun May  2 16:19:36 2021

@author: Qilin Wang
"""

import P144_13_7_1 as mod1

class Shape:
    def what_am_i(self):
        print('I am a Shape')
        
class Square(mod1.Square,Shape):
    pass

class Rectangle(mod1.Rectangle,Shape):
    pass

if __name__ == '__main__':
    t1 = Square(10)
    t1.what_am_i()
    t2 = Rectangle(10,20)
    t2.what_am_i()