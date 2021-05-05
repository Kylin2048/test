# -*- coding: utf-8 -*-
"""
Created on Sun May  2 15:36:36 2021

@author: Qilin Wang
"""

import P144_13_7_1 as mod1

class Square(mod1.Square):
    def change_size(self, n):
        self.a = self.a+n
        self.b = self.a

if __name__ == '__main__':
    t = Square(10)
    print('原边长{}'.format(t.calculate_perimeter()))
    t.change_size(int(input('增加边长：')))
    print('现有边长{}'.format(t.calculate_perimeter()))
    