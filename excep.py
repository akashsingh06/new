# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 01:08:32 2018

@author: sharda
"""

class fact:
    var=10
    def fact(n):
     if (n==0):
        return 1
     else:
        return (n*fact(n-1))
            
try:
    n=int(input("enter any num:"))
    print(fact(10))
finally:
   print("exception occur")