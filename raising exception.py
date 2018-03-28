# -*- coding: utf-8 -*-
"""
Created on Thu Mar  8 14:58:56 2018

@author: sharda
"""

try:
    n=int(input("enter number "))
    r=(n*2)
    print(r)
    raise ValueError
except:
    print("exception occured ")