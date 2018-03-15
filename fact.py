# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 01:01:21 2018

@author: sharda
"""
import sys
sys.setrecursionlimit(1000000)
def fact(n):
    if n==1:
        return 1
    else:
        n=n*fact(n-1)
        return n
n=int(input("enter any number:"))
print(fact(n))