# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 23:02:56 2018

@author: sharda
"""
a=int(input("enter the length: "))
b=[]
def selectionsort(a):
   for i in range(len(list)-1,0,-1):
       pos=0
       c=int(input("enter the elements:"))
       b.append(c)
       for j in range(1,i+1):
           if list[j]>list[pos]:
            pos=j
temp=list[i]
list[i]=list[pos]
list[pos]=temp
print(b)
            
        
            