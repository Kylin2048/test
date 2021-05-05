# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 22:20:54 2021
3.17.3
@author: Qilin Wang
"""

value = eval(input())
if value <= 10:
    print("输入的数不超过10。")
elif value <= 25:
    print("输入的数超过10，不超过25。")
else:
    print("输入的数超过25。")