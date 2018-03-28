# -*- coding: utf-8 -*-
"""
Created on Thu Mar  8 15:32:11 2018

@author: sharda
"""

n=int(input("enter number "))
def fact(n):
    try:
        if(n==0):
            return 1
        else:
            return(n*fact(n-1))
    except:
        print("exception")   
print(fact(n))        