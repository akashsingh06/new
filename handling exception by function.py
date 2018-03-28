# -*- coding: utf-8 -*-
"""
Created on Thu Mar  8 15:14:04 2018

@author: sharda
"""

n=int(input("enter number "))
n1=int(input("enter number "))
def divide(n,n1):
    try:
        r=(n/n1)
        print(r)
    except(ZeroDivisionError,ValueError):
        print("exception occured ")
divide(n,n1)        
    