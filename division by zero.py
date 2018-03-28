# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 13:16:42 2018

@author: sharda
"""

try:
    n1=int(input("enter number"))
    n2=int(input("enter number"))
    r=n1/n2
    print(r)
except(ZeroDivisionError,ValueError):
    print("plz check you enter wrong value & try agian")
