# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 00:27:23 2018

@author: sharda
"""

def binary(a,b):
    lowest=0
    highest=len(a)-1
    while lowest<=highest:
        mid=(lowest+highest)//2
        if (a[mid]==b):
            print("the position is",mid+1)
            break
        elif(a[mid]>b):
            highest=mid-1
        else:
            
            lowest=mid+1
e=[]
c=int(input("enter the total number for list:"))
for i in range(c):
    d=int(input("enter the number:"))
    e.append(d)
a=sorted(e)
print(a)
b=int(input("enter the number you want tonmsearch:"))
binary(a,b)
        