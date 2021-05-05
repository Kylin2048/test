# -*- coding: utf-8 -*-
"""
Created on Sun May  2 14:32:56 2021

@author: Qilin Wang
"""
import csv
my_list = [['Top Gun', 'Risky Business', 'Minority Report'],
           ['Titanic', 'The Revenant', 'Inception'],
           ['Training Day', 'Man on Fire', 'Flight']]
'''
with open('book.csv','w',newline = '') as f:
    w = csv.writer(f, delimiter = ',')
    for x in my_list:
        w.writerow(x)
'''
with open('book.csv','w',newline = '') as f:
    w = csv.writer(f,delimiter = ',')
    w.writerows(my_list)
            
