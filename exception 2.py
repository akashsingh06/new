# -*- coding: utf-8 -*-
"""
Created on Thu Mar  8 01:46:03 2018

@author: sharda
"""

def fact(n):
    if (n==0):
        return 1
    else:
        return (n*fact(n-1))
            
try:
    n=int(input("enter any num:"))
    print(fact(n))
finally:
   print("exception occur")
    