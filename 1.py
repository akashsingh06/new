# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 23:49:38 2018

@author: sharda
"""

try:
    n1=int(input("enter first number:"))
    n2=int(input("enter second number:"))
    r=n1/n2
    print(r)
except ZeroDivisionError:
    print("denominator can not be zero")