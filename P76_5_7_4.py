# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 22:03:03 2021

@author: Qilin Wang
"""

Qilin = {'Height':'178 cm',
         'Colour':'Lightseagreen',
         'Author':'Liu Cixin'}

question = input("What do you want to inquire about? Type: Height/Color/Authur\n")

try:
    print(Qilin[question])
except:
    print("Incorrect inquire!")