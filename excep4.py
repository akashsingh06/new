# -*- coding: utf-8 -*-
"""
Created on Thu Mar  8 02:03:11 2018

@author: sharda
"""

def divide(n1,n2):
   try:
      r=n1/n2
      print(r)
   except:
         print("Exception occur")
n1=int(input("enter first value:"))
n2=int(input("enter sec num:"))
divide(n1,n2)