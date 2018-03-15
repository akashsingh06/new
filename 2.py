# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 00:04:36 2018

@author: sharda
"""

try:
    n1=int(input("enter first number:"))
    n2=int(input("enter second number:"))
    r=n1*n2
    print(r)
except (ZeroDivisionError,ValueError,KeyboardInterrupt):
    print("enetr correct value")