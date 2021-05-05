# -*- coding: utf-8 -*-
"""
Created on Sun May  2 16:33:57 2021

@author: Qilin Wang
"""

class Horse():
    def __init__(self,name,owner):
        self.name = name
        self.owner = owner
        
class Rider():
    def __init__(self,name):
        self.name = name
        
rider_name = ['R1', 'R2', 'R3', 'R4']
horse_name = ['H1', 'H2', 'H3', 'H4']
rider_list = []
for x in rider_name:
    rider_list.append(Rider(x))
horse_list = []
for i,x in enumerate(horse_name):
    horse_list.append(Horse(x,rider_list[i]))

for x in horse_list:
    print(x.owner.name)