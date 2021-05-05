# -*- coding: utf-8 -*-
"""
Created on Sun May  2 14:19:12 2021

@author: Qilin Wang
"""

'''import os
fn = os.path.join('C:''Users','Dell','Desktop','Python','TheSelfTaughtProgrammer','HelloWorld.py')
'''
fn = 'HelloWorld.py'
my_list = ['Next is a code\n']

with open(fn,'r') as f:
    my_list.append(f.read())
print(my_list)
