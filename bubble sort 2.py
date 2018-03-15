# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 23:41:48 2018

@author: sharda
"""

a=int(input("enter the length: "))
b=[]
for i in range(0,a):
    print("enter no of element:")
    c=str(input("enter the elements:"))
    b.append(c)
def bubblesort(nlist):
    for i in range(len(nlist)):
        for j in range(len(nlist)-1-i):
            if nlist[j]>nlist[j+1]:
               temp=nlist[j]
               nlist[j]=nlist[j+1]
               nlist[j+1]=temp
bubblesort(b)
print(b)