# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 13:20:42 2018

@author: sharda
"""

n=int(input("enter a number"))
nn=int(input("enter a number"))
def divide(n,nn):
    try:
        r=(n/nn)
        print(r)
    except(ZeroDivisionError):
        print("exception occured")
    finally:
        print("this is final Block")
print(n,nn)