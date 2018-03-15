# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 00:06:03 2018

@author: sharda
"""

try:
    n1=int(input("enter first number:"))
    n2=int(input("enter second number:"))
    r=n1/n2
    print(r)
except ZeroDivisionError:
    print("denominator cant be zero")
except ValueError:
    print("enter correct value")