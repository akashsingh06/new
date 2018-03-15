# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 00:11:50 2018

@author: sharda
"""

class xyz:
    a=10
    b=20
    def first(self):
        print ("hello")
    def second(self):
        print ("from second")
        
class abc(xyz):
    d=10
    e=80
    def third(self):
        print ("hh")
z=abc()
z.third()
z.first()
print(z.a)
        
    