# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 23:29:59 2018

@author: sharda
"""

class abc(Exception):
     pass
class xyz(Exception):
     pass
a=int(input("enter number"))
try:
    if a>10:
        raise abc
    elif a<10:
        raise xyz
except abc:
     print("number is greater")
except xyz:
     print("number is smaller")        