# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 23:25:46 2018

@author: sharda
"""

def fact(n):
    if n==0:
        return 1
    else:
        n=n*fact(n-1)
        return n
n=int(input("enter any number:"))
print(fact(n))
        