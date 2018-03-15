# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 00:22:13 2018

@author: sharda
""

 def fact(n):
    if(n==1):
        return 1
    else:
        return(n*fact(n-1))
n=int(input("enter no."))
print(fact(n))