# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 23:15:49 2018

@author: sharda
"""

def fib(n):
    if n==0:
        return 0
    if n==1:
        return 1`
    else:
        return(fib(n-1)+fib(n-2))
n=int(input("enter any number:"))
for i in range(n):
   print(fib(i))