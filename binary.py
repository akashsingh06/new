# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 23:59:02 2018

@author: sharda
"""

h=int(input("enter the length of the list:"))
a=[]
for i in range(h):
    u=int(input("enter any number:"))
    a.append(u)
n=int(input("enter the number which has to be find:"))
for i in range(len(a)):
     if(a[i]==n):
         print("it is present and the index is:",i)
         break
else:
    print("not present")