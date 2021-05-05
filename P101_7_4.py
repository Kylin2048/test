# -*- coding: utf-8 -*-
"""
Created on Sun May  2 13:47:43 2021

@author: Qilin Wang
"""
l = [2,3,5,8]
while True:
    st = input('Guess a number in the list, type \'q\' quit.\n')
    if st == 'q':
        break;
    else:
        try:
            n = int(st)
            if n in l:
                print('Yes!')
            else:
                print('No!')
        except:
            print('Error input!')